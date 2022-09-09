from typing import Dict

from pydantic import BaseModel


class Skill(BaseModel):
    __root__: Dict[str, int]
