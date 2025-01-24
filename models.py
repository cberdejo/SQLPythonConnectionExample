from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

# Definición de modelos para SQLModel


class Department(SQLModel, table=True):
    dname: str = Field(..., max_length=20, unique=True)
    dnumber: int = Field(primary_key=True)
    mgr_ssn: Optional[str] = Field(
        default=None, max_length=9, foreign_key="employee.ssn"
    )
    mgr_start_date: str

    employees: List["Employee"] = Relationship(back_populates="department")
    projects: List["Project"] = Relationship(back_populates="department")
    locations: List["DeptLocation"] = Relationship(back_populates="department")


class Employee(SQLModel, table=True):
    fname: str = Field(..., max_length=20)
    minit: Optional[str] = Field(default=None, max_length=1)
    lname: str = Field(..., max_length=20)
    ssn: str = Field(primary_key=True, max_length=9)
    bdate: str
    address: Optional[str] = Field(default=None, max_length=50)
    sex: Optional[str] = Field(default=None, max_length=1)
    salary: Optional[float] = None
    super_ssn: Optional[str] = Field(
        default=None, max_length=9, foreign_key="employee.ssn"
    )
    dno: Optional[int] = Field(default=None, foreign_key="department.dnumber")

    department: Optional[Department] = Relationship(back_populates="employees")
    dependents: List["Dependent"] = Relationship(back_populates="employee")
    works_on: List["WorksOn"] = Relationship(back_populates="employee")


class DeptLocation(SQLModel, table=True):
    dnumber: int = Field(..., foreign_key="department.dnumber", primary_key=True)
    dlocation: str = Field(..., max_length=20, primary_key=True)

    department: Optional[Department] = Relationship(back_populates="locations")


class Project(SQLModel, table=True):
    pname: str = Field(..., max_length=20, unique=True)
    pnumber: int = Field(primary_key=True)
    plocation: str = Field(..., max_length=20)
    dnum: Optional[int] = Field(default=None, foreign_key="department.dnumber")

    department: Optional[Department] = Relationship(back_populates="projects")
    works_on: List["WorksOn"] = Relationship(back_populates="project")


class WorksOn(SQLModel, table=True):
    essn: str = Field(..., foreign_key="employee.ssn", primary_key=True)
    pno: int = Field(..., foreign_key="project.pnumber", primary_key=True)
    hours: Optional[float] = None

    employee: Optional[Employee] = Relationship(back_populates="works_on")
    project: Optional[Project] = Relationship(back_populates="works_on")


class Dependent(SQLModel, table=True):
    essn: str = Field(..., foreign_key="employee.ssn", primary_key=True)
    dependent_name: str = Field(..., max_length=20, primary_key=True)
    sex: Optional[str] = Field(default=None, max_length=1)
    bdate: str
    relationship: str = Field(..., max_length=20)

    employee: Optional[Employee] = Relationship(back_populates="dependents")
