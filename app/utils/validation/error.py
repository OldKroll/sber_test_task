from typing import List

from pydantic import BaseModel


class Error(BaseModel):
    message: str
    type: str


class ErrorResponse(BaseModel):
    detail: List[Error]
