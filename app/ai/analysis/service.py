import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

from app.ai.analysis.models import MeetingAnalysis


class AnalysisService:

    def __init__(self):
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)

        print("Gemini analysis service initialized.")

    def analyze(self, transcript: str) -> MeetingAnalysis:

        prompt = f"""
You are an AI meeting analyst.

Analyze the following meeting transcript.

Extract:
- a concise summary
- important key points
- decisions that were actually made
- action items

For each action item, identify the assignee and deadline
only when they are supported by the transcript.

Do not invent missing information.

TRANSCRIPT:
{transcript}
"""

        for attempt in range(3):

            try:
                response = self.client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt,
                    config={
                        "response_mime_type": "application/json",
                        "response_schema": MeetingAnalysis,
                    }
                )

                return MeetingAnalysis.model_validate_json(
                    response.text
                )

            except ServerError:

                if attempt == 2:
                    raise

                wait_time = 2 ** attempt

                print(
                    f"Gemini unavailable. "
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)