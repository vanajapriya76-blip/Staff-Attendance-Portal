from sqlalchemy import Column, Integer, String, Date
from database import Base

class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String)
    reason = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    status = Column(String, default="Pending")