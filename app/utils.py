from typing import (
    Dict,
    List,
)

from app.schemas.skill import Skill


def get_skills_dict(skills: List[Skill]) -> Dict[str, int]:
    if not skills:
        {}

    return_dict = {}
    for skill in skills:
        skill_name, skill_value = list(skill.__root__.items())[0]
        return_dict[skill_name.lower()] = skill_value

    return return_dict
