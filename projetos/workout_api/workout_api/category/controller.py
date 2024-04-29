from uuid import uuid4
from pydantic import UUID4
from fastapi import APIRouter, status, Body, HTTPException
from workout_api.category.schemas import CategoryIn, CategoryOut
from workout_api.category.models import CategoryModel
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select
from fastapi_pagination import paginate, LimitOffsetPage


router = APIRouter()

@router.post(
        path='/',
        summary="Create new category",
        status_code=status.HTTP_201_CREATED,
        response_model=CategoryOut
)
async def post(
    db_session: DatabaseDependency,
    category_in: CategoryIn = Body(...)
) -> CategoryOut:
    
    category_out = CategoryOut(id=uuid4(), **category_in.model_dump())
    category_model = CategoryModel(**category_out.model_dump())

    db_session.add(category_model)
    await db_session.commit()

    return category_out


@router.get(
        path='/',
        summary="Get all categories",
        status_code=status.HTTP_200_OK,
        response_model=LimitOffsetPage[CategoryOut]
)
async def query(db_session: DatabaseDependency) -> LimitOffsetPage[CategoryOut]:
    categories: list[CategoryOut] = (await db_session.execute(select(CategoryModel))).scalars().all()
    return paginate(categories)


@router.get(
        path='/{id}',
        summary="Get one category by id",
        status_code=status.HTTP_200_OK,
        response_model=CategoryOut
)
async def query_one(id: UUID4, db_session: DatabaseDependency) -> list[CategoryOut]:
    category: CategoryOut = (
        await db_session.execute(select(CategoryModel).filter_by(id=id))
    ).scalars().first()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Category not found on id: {id}")

    return category
