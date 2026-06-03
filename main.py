from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AppError
from app.presentation.api.v1.routes import routers


@asynccontextmanager
async def lifespan(app):
    yield

app = FastAPI(lifespan=lifespan)

for router in routers:
    app.include_router(router, prefix="/api/v1")

@app.get("/health")
async def health():
    return {"message": "Ok"}


@app.exception_handler(AppError)
async def app_exception_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
