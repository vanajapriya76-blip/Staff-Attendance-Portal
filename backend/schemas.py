from pydantic import BaseModel
from datetime import date

class LeaveCreate(BaseModel):
    staff_name: str
    reason: str
    from_date: date
    to_date: date