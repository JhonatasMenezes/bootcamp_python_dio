from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class TrainingCenter(BaseSchema):
    name: Annotated[str, Field(description="Center name", examples="King TC", max_length=20)]
    address: Annotated[str, Field(description="Center address", examples="Rua X, Quadra 2", max_length=60)]
    owner: Annotated[str, Field(description="Center owner identity", examples="Marcos", max_length=30)]