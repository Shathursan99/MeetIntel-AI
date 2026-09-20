import os
import shutil
import tempfile

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.ai.meeting_pipeline.service import MeetingPipelineService


router = APIRouter(
    prefix="/meeting",
    tags=["meeting"],
)

meeting_pipeline = MeetingPipelineService()


@router.post("/analyze")
async def analyze_meeting(
    file: UploadFile = File(...),
    num_speakers: int | None = None
):
    temp_path = None

    try:
        # Keep the uploaded file extension
        suffix = os.path.splitext(file.filename or "")[1]

        # Create temporary file
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            shutil.copyfileobj(file.file, temp_file)
            temp_path = temp_file.name

        # Run complete AI pipeline
        result = meeting_pipeline.process(
            temp_path,
            num_speakers=num_speakers
        )

        return {
            "filename": file.filename,
            "transcript": result["transcript"],
            "segments": result["segments"],
            "analysis": result["analysis"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Meeting analysis failed: {str(e)}"
        )

    finally:
        # Delete temporary audio file
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)