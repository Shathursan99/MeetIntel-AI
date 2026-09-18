import os
if os.name == "nt":
    os.add_dll_directory(r"C:\ffmpeg\bin")

from dotenv import load_dotenv
from pyannote.audio import Pipeline

class DiarizationService:
    def __init__(self):
        load_dotenv()

        hf_token = os.getenv("HF_TOKEN")

        if not hf_token:
            raise ValueError("HF_TOKEN not found in environment.")

        print("Loading speaker diarization model...")

        self.pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-community-1",
            token=hf_token
        )
        print("Model loaded successfully!")
        
    def diarize(self, audio_path: str, num_speakers: int | None = None):
    
        if num_speakers:
            output = self.pipeline(
                audio_path,
                num_speakers=num_speakers
            )
        else:
            output = self.pipeline(audio_path)

        segments = []

        for turn, speaker in output.speaker_diarization:
            segments.append({
                "speaker": speaker,
                "start": round(turn.start, 3),
                "end": round(turn.end, 3)
            })

        return segments