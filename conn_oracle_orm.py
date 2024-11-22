import os
from typing import Optional
from models import Department, Dependent, DeptLocation, Employee, WorksOn
from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine
load_dotenv()

username = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
hostname = os.getenv("ORACLE_HOSTNAME")
sid = os.getenv("ORACLE_SID")


engine = create_engine("oracle+oracledb://{username}:{password}@{hostname}/{sid}")



SQLModel.metadata.create_all(engine)


