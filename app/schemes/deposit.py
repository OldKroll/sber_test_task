from datetime import date, datetime
from typing import Annotated, Any

from pydantic import BaseModel, Field, field_validator


class EntryVector(BaseModel):
    date: Annotated[date, Field(examples=["31.01.2021"])]
    periods: Annotated[int, Field(gt=0, lt=61, examples=[3])]
    amount: Annotated[int, Field(gt=9999, lt=3000001, examples=[10000])]
    rate: Annotated[int, Field(gt=0, lt=9, examples=[6])]

    @field_validator("date", mode="before")
    @classmethod
    def date_validation(cls, value: Any) -> date:
        if not isinstance(value, str):
            raise ValueError(f"Invalid date, must be 'str' with format '%d.%m.%Y'")
        return datetime.strptime(value, "%d.%m.%Y").date()
