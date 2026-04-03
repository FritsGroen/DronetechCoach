from pydantic import BaseModel, Field
from typing import Any

class ChannelContext(BaseModel):
    team_id: str | None = None
    channel_id: str | None = None

class AskRequest(BaseModel):
    message: str = Field(..., min_length=1)
    role: str = Field(default="student")
    conversation_id: str | None = None
    language: str = "nl"
    channel_context: ChannelContext | None = None

class SourceItem(BaseModel):
    document: str
    title: str
    chunk_id: str | None = None

class SafetyResult(BaseModel):
    level: str = "normal"
    escalate: bool = False
    matched_keywords: list[str] = []

class AskResponse(BaseModel):
    answer: str
    category: str
    audience: str
    safety: SafetyResult
    sources: list[SourceItem] = []
    suggested_follow_ups: list[str] = []
    debug: dict[str, Any] | None = None
