from fastapi import APIRouter
from workout_api.athlete.controller import router as athlete
from workout_api.category.controller import router as category
from workout_api.training_center.controller import router as trainingcenter


api_router = APIRouter()
api_router.include_router(athlete, prefix='/athlete', tags=['athletes'])
api_router.include_router(category, prefix='/category', tags=['categories'])
api_router.include_router(trainingcenter, prefix='/trainingcenters', tags=['trainingcenters'])
