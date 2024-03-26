from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.utils.validation.error import ErrorResponse


def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {
        "detail": [
            {
                "message": err["msg"],
                "type": err["type"],
            }
        ]
        for err in exc.errors()
    }
    error_res = ErrorResponse(**errors)
    return JSONResponse(
        content=jsonable_encoder(error_res.detail[0]),
        status_code=status.HTTP_400_BAD_REQUEST,
    )
