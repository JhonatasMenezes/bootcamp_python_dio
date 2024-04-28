from uuid import uuid4
from fastapi import APIRouter, status, Body
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.category.schemas import CategoryIn, CategoryOut

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
) -> CategoryIn:
    
    category_out = CategoryOut(id=uuid4(), **category_in.model_dump())
    breakpoint()

