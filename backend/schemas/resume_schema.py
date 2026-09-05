from pydantic import BaseModel
from typing import List


class ResumeInfo(BaseModel):
    name: str
    email: str
    phone: str
    skills: List[str]