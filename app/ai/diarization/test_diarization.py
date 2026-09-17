import os

if os.name == "nt":
    os.add_dll_directory(r"C:\ffmpeg\bin")
    
from dotenv import load_dotenv
from pyannote.audio import Pipeline


# Load environment variables from .env
load_dotenv()

hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise ValueError("HF_TOKEN not found in .env")


print("Loading speaker diarization model...")

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-community-1",
    token=hf_token
)

print("Model loaded successfully!")


# Audio file containing two or more speakers

audio_file = "app/ai/diarization/test_audio2.wav"

print("Running speaker diarization...")

output = pipeline(
    audio_file,
    num_speakers=2
)
print("\nSpeaker Diarization Results:")

for turn, speaker in output.speaker_diarization:
    print(
        f"{speaker} speaks between "
        f"{turn.start:.3f}s and {turn.end:.3f}s"
    )