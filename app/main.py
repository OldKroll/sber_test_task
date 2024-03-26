from typing import Any

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from app import api
from app.utils.validation.custom_handlers import validation_exception_handler
from app.utils.validation.error import ErrorResponse

app = FastAPI(
    default_response_class=JSONResponse,
    exception_handlers={RequestValidationError: validation_exception_handler},
    responses={
        400: {
            "description": "Validation Error",
            "model": ErrorResponse,
        },
    },
)

app.include_router(api.router)


def custom_openapi() -> dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title, version=app.version, routes=app.routes
    )
    for method in openapi_schema["paths"]:
        try:
            del openapi_schema["paths"][method]["post"]["responses"]["422"]
        except KeyError:
            pass

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
