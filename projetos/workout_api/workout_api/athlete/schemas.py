from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema, OutMixin

class Athlete(BaseSchema):
    name: Annotated[str, Field(description="Athlete name", examples="Jhonatas", max_length=50)]
    cpf: Annotated[str, Field(description="Athlete document", examples="12345678900", max_length=11)]
    age: Annotated[str, Field(description="Athlete age", examples=25)]
    weight: Annotated[PositiveFloat, Field(description="Athlete weight", examples=75.5)]
    height: Annotated[PositiveFloat, Field(description="Athlete height", examples=1.70)]
    gender: Annotated[PositiveFloat, Field(description="Athlete gender", examples="M", max_length=1)]


class AthleteIn(Athlete):
    pass


class AthleteOut(Athlete, OutMixin):
    pass
