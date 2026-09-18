from transformers import pipeline

class SpeechToTextService:
    def __init__(self):
        print("Loading Whisper model...")
        self.pipe = pipeline(
            "automatic-speech-recognition", 
            model="openai/whisper-small"
        )
        
        print("whisper model loading...")
        
    
    def transcribe(self, audio_path: str)-> str:
        print("Transcribing audio..")
        result = self.pipe(
            audio_path,
            return_timestamps=True
        )
        return result