from app.ai.speech_to_text.service import SpeechToTextService
from app.ai.diarization.service import DiarizationService
from app.ai.transcript.merger import merge_transcript_with_speakers
import time

# audio_file = "app/ai/transcript/test_normalized.wav"
audio_file = "app/ai/transcript/test_audio2.wav"

# 1. Load services
stt_service = SpeechToTextService()
diarization_service = DiarizationService()


# 2. Run Whisper
print("\nTranscribing audio...")
start = time.time()
transcription = stt_service.transcribe(audio_file)
print(
    f"Whisper completed in "
    f"{time.time() - start:.2f} seconds"
)
whisper_chunks = transcription["chunks"]

# 3. Run speaker diarization
print("\nDetecting speakers...")
start = time.time()
speaker_segments = diarization_service.diarize(
    audio_file,
    num_speakers=2
)
print(
    f"Diarization completed in "
    f"{time.time() - start:.2f} seconds"
)


# 4. Merge both results
print("\nMerging transcript with speakers...")

result = merge_transcript_with_speakers(
    whisper_chunks,
    speaker_segments
)


# 5. Display final transcript
print("\nFinal Speaker Transcript:\n")

for segment in result:
    print(
        f"[{segment['start']:.1f}s - {segment['end']:.1f}s] "
        f"{segment['speaker']}: {segment['text']}"
    )