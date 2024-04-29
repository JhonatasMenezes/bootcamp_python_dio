from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel
from workout_api.athlete.models import AthleteModel

class CategoryModel(BaseModel):
    __tablename__ = "category"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
    athlete: Mapped['AthleteModel'] = relationship(back_populates='category')