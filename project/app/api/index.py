from fastapi import APIRouter, Depends

from app.config import get_settings, Settings


router = APIRouter()


@router.get('/')
async def index(settings: Settings = Depends(get_settings)):
    return {
        "message": "welcome!",
        "docs": "/docs",
        "environment": settings.environment,
        "testing": settings.testing
    }
