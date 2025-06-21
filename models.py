from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ChocolatinVariableHistory(BaseModel):
    id: int
    module: str
    address: str
    symbol: Optional[str] = None
    data_type: Optional[str] = None
    comment: Optional[str] = None
    value: Optional[str] = None
    timestamp: datetime
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True 