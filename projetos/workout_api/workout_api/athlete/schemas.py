from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from workout_api.category.schemas import CategoryIn
from workout_api.training_center.schemas import TrainingCenterAthlete
from workout_api.contrib.schemas import BaseSchema, OutMixin


class Athlete(BaseSchema):
    name: Annotated[str, Field(description="Athlete's name", example="Jhonatas", max_length=50)]
    cpf: Annotated[str, Field(description="Athlete's document", example="12345678900", max_length=11)]
    age: Annotated[int, Field(description="Athlete's age", example=25)]
    weight: Annotated[PositiveFloat, Field(description="Athlete's weight", example=75.5)]
    height: Annotated[PositiveFloat, Field(description="Athlete's height", example=1.70)]
    gender: Annotated[str, Field(description="Athlete's gender", example="M", max_length=1)]
    category: Annotated[CategoryIn, Field(description="Athlete's category")]
    training_center: Annotated[TrainingCenterAthlete, Field(description="Athlete's training center")]


class AthleteIn(Athlete):
    pass


class AthleteOut(Athlete, OutMixin):
    pass


class AthleteUpdate(BaseSchema):
    name: Annotated[Optional[str], Field(None, description="Athlete's name", example="Jhonatas", max_length=50)]
    age: Annotated[Optional[int], Field(None, description="Athlete's age", example=25)]
