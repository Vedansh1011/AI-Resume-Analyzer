from pydantic import BaseModel
from typing import Any


class JobDescription(BaseModel):
    resume_skills: list[str]
    resume_data: dict[str, Any]
    job_description: str