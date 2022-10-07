from fastapi import APIRouter

from app.api.epg.endpoints import eval

api_router = APIRouter()

api_router.include_router(
    eval.router,
    prefix="/eval",
    tags=["Вычисление eval"],
)
