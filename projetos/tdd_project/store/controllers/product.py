from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Body, Depends, Path
from store.core.exceptions import NotFoundException, InvalidInserctionException
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.usecases.product import ProductUsecase


router = APIRouter(tags=["products"])


@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ProductIn = Body(...), usecase: ProductUsecase = Depends()
) -> ProductOut:
    try:
        return await usecase.create(body=body)
    except InvalidInserctionException as exception:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=exception.message
        )


@router.get(path="/{id}", status_code=status.HTTP_200_OK)
async def get(id: UUID = Path(...), usecase: ProductUsecase = Depends()) -> ProductOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exception.message
        )


@router.get(path="/", status_code=status.HTTP_200_OK)
async def query(
    filter_by: str | None = None,
    op: str | None = None,
    value: float | None = None,
    usecase: ProductUsecase = Depends(),
) -> List[ProductOut]:
    if not filter_by:
        return await usecase.query()
    else:
        try:
            body = {"filter_by": filter_by, "op": op, "value": value}
            return await usecase.query_filter_price_or_quantity(body)
        except InvalidInserctionException as exception:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=exception.message
            )


@router.patch(path="/{id}", status_code=status.HTTP_200_OK)
async def patch(
    id: UUID = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUsecase = Depends(),
) -> ProductUpdateOut:
    try:
        return await usecase.update(id=id, body=body)
    except NotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exception.message
        )


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exception.message
        )
