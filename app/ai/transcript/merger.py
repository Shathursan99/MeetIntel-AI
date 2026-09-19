def merge_transcript_with_speakers(
    whisper_chunks,
    speaker_segments
):
    merged_segments = []

    for chunk in whisper_chunks:

        whisper_start, whisper_end = chunk["timestamp"]
        text = chunk["text"].strip()

        best_speaker = "UNKNOWN"
        best_overlap = 0

        for segment in speaker_segments:

            speaker_start = segment["start"]
            speaker_end = segment["end"]

            overlap_start = max(
                whisper_start,
                speaker_start
            )

            overlap_end = min(
                whisper_end,
                speaker_end
            )

            overlap = max(
                0,
                overlap_end - overlap_start
            )

            if overlap > best_overlap:
                best_overlap = overlap
                best_speaker = segment["speaker"]

        merged_segments.append({
            "speaker": best_speaker,
            "start": whisper_start,
            "end": whisper_end,
            "text": text
        })

    return merged_segments