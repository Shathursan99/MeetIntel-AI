from fastapi import APIRouter
from app.api.v1.transcription import router as transcription_router
from app.api.v1.meeting import router as meeting_router

router = APIRouter()

router.include_router(transcription_router)
router.include_router(meeting_router)