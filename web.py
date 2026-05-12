from fastapi import FastAPI, HTTPException, Depends

from sqlalchemy.orm import Session

from schemas import Employee, EmployeeUpdate

from models import EmployeeDB

from database import engine, SessionLocal, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()


# DATABASE SESSION

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# READ SINGLE EMPLOYEE

@app.get('/employees/{id}')

def get_employee(
    id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail=f"employee with id {id} not found"
        )

    return employee


# READ ALL EMPLOYEES

@app.get('/employees')

def get_all_employees(
    db: Session = Depends(get_db)
):

    employees = db.query(EmployeeDB).all()

    return {
        "employees": employees
    }


# CREATE EMPLOYEE

@app.post('/employees')

def add_employee(
    new_employee: Employee,
    db: Session = Depends(get_db)
):

    existing_employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == new_employee.id
    ).first()

    if existing_employee:

        raise HTTPException(
            status_code=400,
            detail="employee id already exists"
        )

    employee = EmployeeDB(

        id=new_employee.id,

        emp_name=new_employee.emp_name,

        age=new_employee.age,

        rating=new_employee.rating,

        dept=new_employee.dept
    )

    db.add(employee)

    db.commit()

    db.refresh(employee)

    return {
        "message": "employee added successfully",
        "employee": employee
    }


# FULL UPDATE (PUT)

@app.put('/employees/{id}')

def put_employee(
    id: int,
    new_info: Employee,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail=f"employee with id {id} not found"
        )

    employee.emp_name = new_info.emp_name

    employee.age = new_info.age

    employee.rating = new_info.rating

    employee.dept = new_info.dept

    db.commit()

    db.refresh(employee)

    return {
        "message": "employee updated successfully",
        "employee": employee
    }


# PARTIAL UPDATE (PATCH)

@app.patch('/employees/{id}')

def patch_employee(
    id: int,
    partial_info: EmployeeUpdate,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail=f"employee with id {id} not found"
        )

    updates = partial_info.model_dump(exclude_unset=True)

    for key, value in updates.items():

        setattr(employee, key, value)

    db.commit()

    db.refresh(employee)

    return {
        "message": "employee info updated",
        "employee": employee
    }


# DELETE EMPLOYEE

@app.delete('/employees/{id}')

def delete_employee(
    id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail=f"employee with id {id} not found"
        )

    db.delete(employee)

    db.commit()

    return {
        "message": f"employee {id} deleted successfully"
    }