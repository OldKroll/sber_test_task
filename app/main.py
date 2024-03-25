from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app import api

app = FastAPI(default_response_class=JSONResponse)

app.include_router(api.router)
