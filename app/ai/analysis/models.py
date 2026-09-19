from pydantic import BaseModel
from typing import Optional


class ActionItem(BaseModel):
    task: str
    assignee: Optional[str] = None
    deadline: Optional[str] = None


class MeetingAnalysis(BaseModel):
    summary: str
    key_points: list[str]
    decisions: list[str]
    action_items: list[ActionItem]