import os
import tempfile
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.ai.speech_to_text.service import SpeechToTextService

router = APIRouter(
    prefix="/transcription",
    tags=["transcription"],
)

stt_service = SpeechToTextService()

@router.post("/")
async def transcribe_audio(file: UploadFile = File(...)):
    allowed_types = [
        "audio/wav",
        "audio/mpeg",
        "audio/mp3",
        "audio/x-wav"
    ]  
     
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Only WAV, MP3, and M4A files are allowed."
        )

    temp_path=None
    
    try:
        # Get original file extension
        suffix = os.path.splitext(file.filename or "")[1]

        # Create temporary audio file
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            content = await file.read()
            temp_file.write(content)

            temp_path = temp_file.name

        # Send temporary file to Whisper
        text = stt_service.transcribe(temp_path)
        
        return{
            "filename": file.filename,
            "transcription": text
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Transcription failed: {str(e)}"
        )
        
    finally:
        # Delete temporary audio file
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)