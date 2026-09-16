from service import SpeechToTextService

stt_service = SpeechToTextService()
print("starting transcription...")
text = stt_service.trnscribe("test_audio2.mp3")
print(f"Transcribed text: {text}")