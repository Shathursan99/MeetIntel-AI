from app.ai.diarization.service import DiarizationService

service = DiarizationService()
audio_file = "app/ai/diarization/test_audio2.wav"

result = service.diarize(
    audio_file,
    num_speakers=2
)
print("\nSpeaker Diarization Results:")
for segment in result:
    print(
        f"{segment['speaker']} speaks between "
        f"{segment['start']}s and {segment['end']}s"
    )