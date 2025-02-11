from typing import Optional

from pydantic import BaseModel, Field


class GradeStatisticResponse(BaseModel):
    count: int = Field(gt=0)
    min: Optional[int] = None
    max: Optional[int] = None
    avg: Optional[int] = None
