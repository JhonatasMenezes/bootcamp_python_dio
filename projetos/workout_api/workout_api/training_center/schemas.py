from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema


class TrainingCenterIn(BaseSchema):
    name: Annotated[str, Field(description="Center's name", example="King TC", max_length=20)]
    address: Annotated[str, Field(description="Center's address", example="Rua X, Quadra 2", max_length=60)]
    owner: Annotated[str, Field(description="Identity of the center owner", example="Marcos", max_length=30)]


class TrainingCenterAthlete(BaseSchema):
    name: Annotated[str, Field(description="Center's name", example="King TC", max_length=20)]


class TrainingCenterOut(TrainingCenterIn):
    id: Annotated[UUID4, Field(description="Training center identifier")]
