from app.ai.analysis.service import AnalysisService


transcript = """
SPEAKER_00: We need to finish the login API by Friday.

SPEAKER_01: Okay, I'll handle the backend implementation.

SPEAKER_00: Great. Let's review the completed API on Monday.

SPEAKER_01: I'll also prepare the API documentation before the review.
"""


service = AnalysisService()

print("\nAnalyzing meeting...")

result = service.analyze(transcript)

print("\nMeeting Analysis:\n")
print(result.model_dump_json(indent=2))