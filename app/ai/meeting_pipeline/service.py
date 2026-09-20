from app.ai.speech_to_text.service import SpeechToTextService
from app.ai.diarization.service import DiarizationService
from app.ai.transcript.merger import merge_transcript_with_speakers
from app.ai.analysis.service import AnalysisService


class MeetingPipelineService:

    def __init__(self):
        self.stt_service = SpeechToTextService()
        self.diarization_service = DiarizationService()
        self.analysis_service = AnalysisService()

    def process(self, audio_path: str, num_speakers: int | None = None):

        # 1. Transcribe
        transcription = self.stt_service.transcribe(audio_path)
        whisper_chunks = transcription["chunks"]

        # 2. Speaker diarization
        speaker_segments = self.diarization_service.diarize(
            audio_path,
            num_speakers=num_speakers
        )

        # 3. Merge speakers + transcript
        merged_segments = merge_transcript_with_speakers(
            whisper_chunks,
            speaker_segments
        )

        # 4. Create transcript for Gemini
        speaker_transcript = "\n".join(
            f"{segment['speaker']}: {segment['text']}"
            for segment in merged_segments
        )

        # 5. Analyze with Gemini
        analysis = self.analysis_service.analyze(
            speaker_transcript
        )

        return {
            "transcript": speaker_transcript,
            "segments": merged_segments,
            "analysis": analysis
        }