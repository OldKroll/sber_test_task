from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import fastapi.openapi.utils as f_utils

from app import api

app = FastAPI(default_response_class=JSONResponse)

app.include_router(api.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"error": exc.errors()}
    )
