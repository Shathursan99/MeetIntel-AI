from fastapi import FastAPI

from app.api.v1.router import router as api_v1_router


app = FastAPI(
    title="MeetIntel AI",
    description="AI-powered Meeting and Interview Analyzer",
    version="0.1.0"
)


app.include_router(
    api_v1_router,
    prefix="/api/v1"
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "MeetIntel AI"
    }