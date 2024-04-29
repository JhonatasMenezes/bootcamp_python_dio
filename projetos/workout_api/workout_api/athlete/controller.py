from typing import Dict
from uuid import uuid4
from pydantic import UUID4
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, status, Body
from workout_api.training_center.models import TrainingCenterModel
from workout_api.athlete.schemas import AthleteIn, AthleteOut, AthleteUpdate
from workout_api.athlete.models import AthleteModel
from workout_api.category.models import CategoryModel
from workout_api.contrib.dependencies import DatabaseDependency
from fastapi_pagination import paginate, LimitOffsetPage

router = APIRouter()

@router.post(
        path='/',
        summary="Create new athlete",
        status_code=status.HTTP_201_CREATED,
        response_model=LimitOffsetPage
)
async def post(
    db_session: DatabaseDependency,
    athlete_in: AthleteIn = Body(...)
):      

    category_name = athlete_in.category.name
    training_center_name = athlete_in.training_center.name

    category = (await db_session.execute(
        select(CategoryModel).filter_by(name=category_name))
    ).scalars().first()
    
    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"The category {category_name} was not found."
            )

    training_center = (await db_session.execute(
        select(TrainingCenterModel).filter_by(name=training_center_name))
    ).scalars().first()
    
    if not training_center:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"The training center {training_center_name} was not found."
            )

    try:
        athlete_out = AthleteOut(id=uuid4(), created_at=datetime.now(timezone.utc), **athlete_in.model_dump())
        athlete_model = AthleteModel(**athlete_out.model_dump(exclude={'category', 'training_center'}))
        athlete_model.category_id = category.pk_id
        athlete_model.tc_id = training_center.pk_id
        db_session.add(athlete_model)
        await db_session.commit()
    except IntegrityError:
        cpf = athlete_in.cpf
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f"Already there are an athlete registered with cpf: {cpf}"
        )


    return athlete_out


@router.get(
        path='/',
        summary="Get all athletes",
        status_code=status.HTTP_200_OK,
        response_model=LimitOffsetPage[Dict]
)
async def query_all_athletes(db_session: DatabaseDependency) -> LimitOffsetPage[Dict]:
    athletes: list[AthleteOut] = (await db_session.execute(select(AthleteModel))).scalars().all()
    
    result = [AthleteOut.model_validate(athlete) for athlete in athletes]
    response = [{
        "name": athlete.name, 
        "training_center": athlete.training_center.name,
        "category": athlete.category.name
        } for athlete in result] 

    return paginate(response)


@router.get(
        path='/{id}',
        summary="Get one athlete by id",
        status_code=status.HTTP_200_OK,
        response_model=AthleteOut
)
async def query_athlete_by_id(id: UUID4, db_session: DatabaseDependency) -> list[AthleteOut]:
    athlete: AthleteOut = (
        await db_session.execute(select(AthleteModel).filter_by(id=id))
    ).scalars().first()

    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Athlete not found on id: {id}"
            )

    return athlete


@router.get(
        path='/name/{name}',
        summary="Get one athlete by name",
        status_code=status.HTTP_200_OK,
        response_model=AthleteOut
)
async def query_athlete_by_name(name: str, db_session: DatabaseDependency) -> list[AthleteOut]:
    athlete: AthleteOut = (
        await db_session.execute(select(AthleteModel).filter_by(name=name))
    ).scalars().first()

    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Athlete not found with name: {name}"
            )

    return athlete


@router.get(
        path='/cpf/{cpf}',
        summary="Get one athlete by name",
        status_code=status.HTTP_200_OK,
        response_model=AthleteOut
)
async def query_athlete_by_cpf(cpf: str, db_session: DatabaseDependency) -> list[AthleteOut]:
    athlete: AthleteOut = (
        await db_session.execute(select(AthleteModel).filter_by(cpf=cpf))
    ).scalars().first()

    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Athlete not found with cpf: {cpf}"
            )

    return athlete


@router.patch(
        path='/{id}',
        summary="Edit one athlete by id",
        status_code=status.HTTP_200_OK,
        response_model=AthleteOut
)
async def query_update_athlete_by_id(id: UUID4, db_session: DatabaseDependency, athlete_up: AthleteUpdate = Body(...)) -> list[AthleteOut]:
    athlete: AthleteOut = (
        await db_session.execute(select(AthleteModel).filter_by(id=id))
    ).scalars().first()

    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Athlete not found on id: {id}"
            )

    athlete_update = athlete_up.model_dump(exclude_unset=True)
    for key, value in athlete_update.items():
        setattr(athlete, key, value)
    
    await db_session.commit()
    await db_session.refresh(athlete)

    return athlete


@router.delete(
        path='/{id}',
        summary="Get one athlete by id",
        status_code=status.HTTP_204_NO_CONTENT
)
async def query_one(id: UUID4, db_session: DatabaseDependency) -> None:
    athlete: AthleteOut = (
        await db_session.execute(select(AthleteModel).filter_by(id=id))
    ).scalars().first()

    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Athlete not found on id: {id}"
            )

    await db_session.delete(athlete)
    await db_session.commit()
