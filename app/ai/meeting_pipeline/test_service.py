from app.ai.meeting_pipeline.service import MeetingPipelineService


audio_file = "app/ai/diarization/test_audio2.wav"

print("Starting Meeting Pipeline...")

pipeline = MeetingPipelineService()

result = pipeline.process(
    audio_file,
    num_speakers=2
)

print("\n========== TRANSCRIPT ==========\n")
print(result["transcript"])

print("\n========== SEGMENTS ==========\n")

for segment in result["segments"]:
    print(
        f"[{segment['start']}s - {segment['end']}s] "
        f"{segment['speaker']}: {segment['text']}"
    )

print("\n========== AI ANALYSIS ==========\n")
print(
    result["analysis"].model_dump_json(indent=2)
)