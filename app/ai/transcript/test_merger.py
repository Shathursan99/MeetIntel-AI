from app.ai.transcript.merger import merge_transcript_with_speakers


whisper_chunks = [
    {
        "timestamp": (0.0, 3.0),
        "text": "Hello, David. How are you today?"
    },
    {
        "timestamp": (3.0, 6.0),
        "text": "I'm good. Thank you."
    }
]


speaker_segments = [
    {
        "speaker": "SPEAKER_00",
        "start": 0.638,
        "end": 2.545
    },
    {
        "speaker": "SPEAKER_01",
        "start": 3.946,
        "end": 5.363
    }
]


result = merge_transcript_with_speakers(
    whisper_chunks,
    speaker_segments
)


for segment in result:
    print(
        f"{segment['speaker']}: "
        f"{segment['text']}"
    )