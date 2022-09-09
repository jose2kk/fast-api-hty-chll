import uuid
from datetime import datetime
from typing import (
    NewType,
    Optional,
)

from pydantic import BaseModel

CompanyId = NewType("CompanyId", uuid.UUID)


class CompanyCreateModel(BaseModel):
    name: str


class CompanyModel(BaseModel):
    id: CompanyId
    name: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class CompanyUpdateModel(BaseModel):
    name: Optional[str]
