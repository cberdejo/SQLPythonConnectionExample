import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
hostname = os.getenv("ORACLE_HOSTNAME")
sid = os.getenv("ORACLE_SID")

connection = oracledb.connect(user=username, password=password, host=hostname, sid=sid)
cursor = connection.cursor()

try:
    # Eliminar tablas existentes
    tables = [
        "works_on",
        "dependent",
        "dept_locations",
        "project",
        "employee",
        "department",
    ]
    for table in tables:
        try:
            cursor.execute(f"DROP TABLE {table} CASCADE CONSTRAINTS")
        except oracledb.DatabaseError:
            pass  # Si la tabla no existe, continuamos

    # Crear tablas sin claves foráneas
    cursor.execute("""
    CREATE TABLE department (
        dname VARCHAR2(20) NOT NULL UNIQUE,
        dnumber NUMBER(10) PRIMARY KEY,
        mgr_ssn VARCHAR2(9),
        mgr_start_date DATE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE employee (
        fname VARCHAR2(20) NOT NULL,
        minit VARCHAR2(1),
        lname VARCHAR2(20) NOT NULL,
        ssn VARCHAR2(9) PRIMARY KEY,
        bdate DATE NOT NULL,
        address VARCHAR2(50),
        sex CHAR(1) CHECK (sex IN ('M', 'F')),
        salary NUMBER(10, 2),
        super_ssn VARCHAR2(9),
        dno NUMBER(10)
     
    )
    """)

    cursor.execute("""
    CREATE TABLE dept_locations (
        dnumber NUMBER(10) NOT NULL,
        dlocation VARCHAR2(20) NOT NULL,
        PRIMARY KEY (dnumber, dlocation)
    )
    """)

    cursor.execute("""
    CREATE TABLE project (
        pname VARCHAR2(20) NOT NULL UNIQUE,
        pnumber NUMBER(10) PRIMARY KEY,
        plocation VARCHAR2(20) NOT NULL,
        dnum NUMBER(10)
        
    )
    """)

    cursor.execute("""
    CREATE TABLE works_on (
        essn VARCHAR2(9) NOT NULL,
        pno NUMBER(10) NOT NULL,
        hours NUMBER(5, 2),
        PRIMARY KEY (essn, pno)
    )
    """)

    cursor.execute("""
    CREATE TABLE dependent (
        essn VARCHAR2(9) NOT NULL,
        dependent_name VARCHAR2(20) NOT NULL,
        sex CHAR(1) CHECK (sex IN ('M', 'F')),
        bdate DATE NOT NULL,
        relationship VARCHAR2(20) NOT NULL,
        PRIMARY KEY (essn, dependent_name)
    )
    """)

    # Insertar datos
    data = [
        # Department
        "INSERT INTO department VALUES ('Research', 5, '333445555', TO_DATE('1978-05-22', 'YYYY-MM-DD'))",
        "INSERT INTO department VALUES ('Administration', 4, '987654321', TO_DATE('1985-01-01', 'YYYY-MM-DD'))",
        "INSERT INTO department VALUES ('Headquarters', 1, '888665555', TO_DATE('1971-06-19', 'YYYY-MM-DD'))",
        # Employee
        "INSERT INTO employee VALUES ('John', 'B', 'Smith', '123456789', TO_DATE('1955-01-09', 'YYYY-MM-DD'), '731 Fondren, Houston,TX', 'M', 30000, '333445555', 5)",
        "INSERT INTO employee VALUES ('Franklin', 'T', 'Wong', '333445555', TO_DATE('1945-12-08', 'YYYY-MM-DD'), '638 Voss, Houston,TX', 'M', 40000, '888665555', 5)",
        "INSERT INTO employee VALUES ('Alicia', 'J', 'Zelaya', '999887777', TO_DATE('1958-07-19', 'YYYY-MM-DD'), '3321 Castle, Spring,TX', 'F', 25000, '987654321', 4)",
        "INSERT INTO employee VALUES ('Jennifer', 'S', 'Wallace', '987654321', TO_DATE('1931-06-20', 'YYYY-MM-DD'), '291 Berry, Bellaire,TX', 'F', 43000, '888665555', 4)",
        "INSERT INTO employee VALUES ('Ramesh', 'K', 'Narayan', '666884444', TO_DATE('1952-09-15', 'YYYY-MM-DD'), '975 Fire Oak, Humble,TX', 'M', 38000, '333445555', 5)",
        "INSERT INTO employee VALUES ('Joyce', 'A', 'English', '453453453', TO_DATE('1962-07-31', 'YYYY-MM-DD'), '5631 Rice, Houston, TX', 'F', 25000, '333445555', 5)",
        "INSERT INTO employee VALUES ('Ahmad', 'V', 'Jabbar', '987987987', TO_DATE('1959-03-29', 'YYYY-MM-DD'), '980 Dallas, Houston,TX', 'M', 25000, '987654321', 4)",
        "INSERT INTO employee VALUES ('James', 'E', 'Borg', '888665555', TO_DATE('1927-11-10', 'YYYY-MM-DD'), '450 Stone, Houston,TX', 'M', 55000, null, 1)",
        # Project
        "INSERT INTO project VALUES ('ProductX', 1, 'Bellaire',  5)",
        "INSERT INTO project VALUES ('ProductY', 2, 'Sugarland', 5)",
        "INSERT INTO project VALUES ('ProductZ', 3, 'Houston', 5)",
        "INSERT INTO project VALUES ('Computerization', 10, 'Stafford', 4)",
        "INSERT INTO project VALUES ('Reorganization', 20, 'Houston', 1)",
        "INSERT INTO project VALUES ('Newbenefits', 30,  'Stafford', 4)",
        # Works_on
        "INSERT INTO works_on VALUES ('123456789', 1,  32.5)",
        "INSERT INTO works_on VALUES ('123456789', 2,  7.5)",
        "INSERT INTO works_on VALUES ('666884444', 3,  40.0)",
        "INSERT INTO works_on VALUES ('453453453', 1,  20.0)",
        "INSERT INTO works_on VALUES ('453453453', 2,  20.0)",
        "INSERT INTO works_on VALUES ('333445555', 2,  10.0)",
        "INSERT INTO works_on VALUES ('333445555', 3,  10.0)",
        "INSERT INTO works_on VALUES ('333445555', 10, 10.0)",
        "INSERT INTO works_on VALUES ('333445555', 20, 10.0)",
        "INSERT INTO works_on VALUES ('999887777', 30, 30.0)",
        "INSERT INTO works_on VALUES ('999887777', 10, 10.0)",
        "INSERT INTO works_on VALUES ('987987987', 10, 35.0)",
        "INSERT INTO works_on VALUES ('987987987', 30, 5.0)",
        "INSERT INTO works_on VALUES ('987654321', 30, 20.0)",
        "INSERT INTO works_on VALUES ('987654321', 20, 15.0)",
        "INSERT INTO works_on VALUES ('888665555', 20, null)",
        # Dependent
        "INSERT INTO dependent VALUES ('333445555','Alice','F',TO_DATE('1976-04-05', 'YYYY-MM-DD'),'Daughter')",
        "INSERT INTO dependent VALUES ('333445555','Theodore','M',TO_DATE('1973-10-25', 'YYYY-MM-DD'),'Son')",
        "INSERT INTO dependent VALUES ('333445555','Joy','F',TO_DATE('1948-05-03', 'YYYY-MM-DD'),'Spouse')",
        "INSERT INTO dependent VALUES ('987654321','Abner','M',TO_DATE('1932-02-29', 'YYYY-MM-DD'),'Spouse')",
        "INSERT INTO dependent VALUES ('123456789','Michael','M',TO_DATE('198-01-01', 'YYYY-MM-DD'),'Son')",
        "INSERT INTO dependent VALUES ('123456789','Alice','F', TO_DATE('1978-12-31', 'YYYY-MM-DD'),'Daughter')",
        "INSERT INTO dependent VALUES ('123456789','Elizabeth','F',TO_DATE('1957-05-05', 'YYYY-MM-DD'),'Spouse')",
        # Dept_locations
        "INSERT INTO dept_locations VALUES (1, 'Houston')",
        "INSERT INTO dept_locations VALUES (4, 'Stafford')",
        "INSERT INTO dept_locations VALUES (5, 'Bellaire')",
        "INSERT INTO dept_locations VALUES (5, 'Sugarland')",
        "INSERT INTO dept_locations VALUES (5, 'Houston')",
    ]

    for statement in data:
        cursor.execute(statement)

    # Agregar claves foráneas con ALTER TABLE
    cursor.execute("""
    ALTER TABLE department
    ADD CONSTRAINT fk_department_mgr
    FOREIGN KEY (mgr_ssn) REFERENCES employee(ssn)
    """)

    cursor.execute("""
    ALTER TABLE employee
    ADD CONSTRAINT fk_employee_supervisor
    FOREIGN KEY (super_ssn) REFERENCES employee(ssn)
    """)

    cursor.execute("""
    ALTER TABLE employee
    ADD CONSTRAINT fk_employee_department
    FOREIGN KEY (dno) REFERENCES department(dnumber)
    """)

    cursor.execute("""
    ALTER TABLE dept_locations
    ADD CONSTRAINT fk_dept_locations_department
    FOREIGN KEY (dnumber) REFERENCES department(dnumber)
    """)

    cursor.execute("""
    ALTER TABLE project
    ADD CONSTRAINT fk_project_department
    FOREIGN KEY (dnum) REFERENCES department(dnumber)
    """)

    cursor.execute("""
    ALTER TABLE works_on
    ADD CONSTRAINT fk_works_on_employee
    FOREIGN KEY (essn) REFERENCES employee(ssn)
    """)

    cursor.execute("""
    ALTER TABLE works_on
    ADD CONSTRAINT fk_works_on_project
    FOREIGN KEY (pno) REFERENCES project(pnumber)
    """)

    cursor.execute("""
    ALTER TABLE dependent
    ADD CONSTRAINT fk_dependent_employee
    FOREIGN KEY (essn) REFERENCES employee(ssn)
    """)

    # Confirmar transacciones
    connection.commit()

except Exception as e:
    print("Error:", e)
    connection.rollback()

finally:
    cursor.close()
    connection.close()
