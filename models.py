from sqlalchemy import Column, Integer, String
from database import Base

class EmployeeDB(Base):
    __tablename__ = "employees"
    id= Column(Integer,primary_key=True, index=True)
    emp_name=Column(String)
    age = Column(Integer)
    rating=Column(Integer)
    dept = Column(String) 