import os
from typing import Optional
from models import Department, Dependent, DeptLocation, Employee, WorksOn, Project
from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine

load_dotenv()


# Get environment variables
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
hostname = os.getenv("DB_HOSTNAME")
sid = os.getenv("DB_SID")
port = os.getenv("DB_PORT")


def create_connection(provider: str):
    # Validate provider
    if provider not in ["oracle", "postgres"]:
        raise ValueError("Providers allowed: 'oracle', 'postgres'")

    # Choose protocol based on provider
    protocol = "oracle+oracledb" if provider == "oracle" else "postgresql+psycopg"

    # Create database connection URL
    database_url = f"{protocol}://{username}:{password}@{hostname}:{port}/{sid}"
    print(database_url)
    # Create SQLAlchemy engine
    engine = create_engine(database_url)

    # Create tables from SQLModel metadata
    SQLModel.metadata.create_all(engine)

    return engine


def init_data(engine):
    with Session(engine) as session:
        # Insertar departamentos
        department_1 = Department(
            dname="Research",
            dnumber=5,
            mgr_ssn="333445555",
            mgr_start_date="1978-05-22",
        )
        department_2 = Department(
            dname="Administration",
            dnumber=4,
            mgr_ssn="987654321",
            mgr_start_date="1985-01-01",
        )
        department_3 = Department(
            dname="Headquarters",
            dnumber=1,
            mgr_ssn="888665555",
            mgr_start_date="1971-06-19",
        )

        session.add_all([department_1, department_2, department_3])

        # Insertar empleados
        employees = [
            Employee(
                fname="John",
                minit="B",
                lname="Smith",
                ssn="123456789",
                bdate="1955-01-09",
                address="731 Fondren, Houston,TX",
                sex="M",
                salary=30000,
                super_ssn="333445555",
                dno=5,
            ),
            Employee(
                fname="Franklin",
                minit="T",
                lname="Wong",
                ssn="333445555",
                bdate="1945-12-08",
                address="638 Voss, Houston,TX",
                sex="M",
                salary=40000,
                super_ssn="888665555",
                dno=5,
            ),
            Employee(
                fname="Alicia",
                minit="J",
                lname="Zelaya",
                ssn="999887777",
                bdate="1958-07-19",
                address="3321 Castle, Spring,TX",
                sex="F",
                salary=25000,
                super_ssn="987654321",
                dno=4,
            ),
            Employee(
                fname="Jennifer",
                minit="S",
                lname="Wallace",
                ssn="987654321",
                bdate="1931-06-20",
                address="291 Berry, Bellaire,TX",
                sex="F",
                salary=43000,
                super_ssn="888665555",
                dno=4,
            ),
            Employee(
                fname="Ramesh",
                minit="K",
                lname="Narayan",
                ssn="666884444",
                bdate="1952-09-15",
                address="975 Fire Oak, Humble,TX",
                sex="M",
                salary=38000,
                super_ssn="333445555",
                dno=5,
            ),
            Employee(
                fname="Joyce",
                minit="A",
                lname="English",
                ssn="453453453",
                bdate="1962-07-31",
                address="5631 Rice, Houston, TX",
                sex="F",
                salary=25000,
                super_ssn="333445555",
                dno=5,
            ),
            Employee(
                fname="Ahmad",
                minit="V",
                lname="Jabbar",
                ssn="987987987",
                bdate="1959-03-29",
                address="980 Dallas, Houston,TX",
                sex="M",
                salary=25000,
                super_ssn="987654321",
                dno=4,
            ),
            Employee(
                fname="James",
                minit="E",
                lname="Borg",
                ssn="888665555",
                bdate="1927-11-10",
                address="450 Stone, Houston,TX",
                sex="M",
                salary=55000,
                super_ssn=None,
                dno=1,
            ),
        ]
        session.add_all(employees)

        # Insertar proyectos
        projects = [
            Project(pname="ProductX", pnumber=1, plocation="Bellaire", dnum=5),
            Project(pname="ProductY", pnumber=2, plocation="Sugarland", dnum=5),
            Project(pname="ProductZ", pnumber=3, plocation="Houston", dnum=5),
            Project(pname="Computerization", pnumber=10, plocation="Stafford", dnum=4),
            Project(pname="Reorganization", pnumber=20, plocation="Houston", dnum=1),
            Project(pname="Newbenefits", pnumber=30, plocation="Stafford", dnum=4),
        ]
        session.add_all(projects)

        # Insertar asignaciones de trabajos
        works_on = [
            WorksOn(essn="123456789", pno=1, hours=32.5),
            WorksOn(essn="123456789", pno=2, hours=7.5),
            WorksOn(essn="666884444", pno=3, hours=40.0),
            WorksOn(essn="453453453", pno=1, hours=20.0),
            WorksOn(essn="453453453", pno=2, hours=20.0),
            WorksOn(essn="333445555", pno=2, hours=10.0),
            WorksOn(essn="333445555", pno=3, hours=10.0),
            WorksOn(essn="333445555", pno=10, hours=10.0),
            WorksOn(essn="333445555", pno=20, hours=10.0),
            WorksOn(essn="999887777", pno=30, hours=30.0),
            WorksOn(essn="999887777", pno=10, hours=10.0),
            WorksOn(essn="987987987", pno=10, hours=35.0),
            WorksOn(essn="987987987", pno=30, hours=5.0),
            WorksOn(essn="987654321", pno=30, hours=20.0),
            WorksOn(essn="987654321", pno=20, hours=15.0),
            WorksOn(essn="888665555", pno=20, hours=None),
        ]
        session.add_all(works_on)

        # Insertar dependientes
        dependents = [
            Dependent(
                essn="333445555",
                dependent_name="Alice",
                sex="F",
                bdate="1976-04-05",
                relationship="Daughter",
            ),
            Dependent(
                essn="333445555",
                dependent_name="Theodore",
                sex="M",
                bdate="1973-10-25",
                relationship="Son",
            ),
            Dependent(
                essn="333445555",
                dependent_name="Joy",
                sex="F",
                bdate="1948-05-03",
                relationship="Spouse",
            ),
            Dependent(
                essn="987654321",
                dependent_name="Abner",
                sex="M",
                bdate="1932-02-29",
                relationship="Spouse",
            ),
            Dependent(
                essn="123456789",
                dependent_name="Michael",
                sex="M",
                bdate="1980-01-01",
                relationship="Son",
            ),
            Dependent(
                essn="123456789",
                dependent_name="Alice",
                sex="F",
                bdate="1978-12-31",
                relationship="Daughter",
            ),
            Dependent(
                essn="123456789",
                dependent_name="Elizabeth",
                sex="F",
                bdate="1957-05-05",
                relationship="Spouse",
            ),
        ]
        session.add_all(dependents)

        # Insertar ubicaciones de departamentos
        dept_locations = [
            DeptLocation(dnumber=1, dlocation="Houston"),
            DeptLocation(dnumber=4, dlocation="Stafford"),
            DeptLocation(dnumber=5, dlocation="Bellaire"),
            DeptLocation(dnumber=5, dlocation="Sugarland"),
            DeptLocation(dnumber=5, dlocation="Houston"),
        ]
        session.add_all(dept_locations)

        # Confirmar transacciones
        session.commit()



# Ejecución de conexión e inicialización
if __name__ == "__main__":
    engine = create_connection("postgres")
    init_data(engine)