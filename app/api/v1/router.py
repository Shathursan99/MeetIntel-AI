from fastapi import APIRouter
from app.api.v1.transcription import router as transcription_router

router = APIRouter()

router.include_router(transcription_router)