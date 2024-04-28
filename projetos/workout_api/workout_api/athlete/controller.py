from fastapi import APIRouter, status, Body
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.athlete.schemas import AthleteIn

router = APIRouter()

@router.post(
        path='/',
        summary="Create new athlete",
        status_code=status.HTTP_201_CREATED
)
async def post(
    db_session: DatabaseDependency,
    athlete_in: AthleteIn = Body(...)):
    pass
