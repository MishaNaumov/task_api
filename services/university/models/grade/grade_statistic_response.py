from typing import Optional

from pydantic import BaseModel, Field


class GradeStatisticResponse(BaseModel):
    count: int = Field(ge=0)
    min: Optional[int]
    max: Optional[int]
    avg: Optional[int]
