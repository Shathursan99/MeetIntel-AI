import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()
class SpeechToTextService:
    def __init__(self):
        hf_token = os.getenv("HF_TOKEN")
        print("Loading Whisper model...")
        self.pipe = pipeline(
            "automatic-speech-recognition", 
            model="openai/whisper-small",
            token=hf_token,
            chunk_length_s=30
        )
        
        print("whisper model loading...")
        
    
    def transcribe(self, audio_path: str)-> str:
        print("Transcribing audio...")
        result = self.pipe(
            audio_path,
            return_timestamps=True,
            generate_kwargs={
                "language": "en",
                "task": "transcribe"
            }
        )
        return result