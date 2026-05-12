from pydantic import BaseModel


class Employee(BaseModel):
    emp_name:str
    id : int
    age:int
    rating:int
    dept:str
    
from typing import Optional    
class EmployeeUpdate(BaseModel):

    emp_name: Optional[str] = None
    id: Optional[int] = None
    age: Optional[int] = None
    rating: Optional[int] = None
    dept: Optional[str] = None    