from app.ai.speech_to_text.service import SpeechToTextService

stt_service = SpeechToTextService()
print("starting transcription...")
result = stt_service.transcribe("app/ai/diarization/test_audio2.wav")
print("\nFull transcription:")
print(result["text"])

print("\nTimestamped chunks:")

for chunk in result["chunks"]:
    print(
        chunk["timestamp"],
        "->",
        chunk["text"]
    )