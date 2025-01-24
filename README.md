[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Project Title: Oracle Database Setup Script
This project contains  Python scripts to set up an Oracle database schema with predefined tables, constraints, and sample data. The script uses oracledb and dotenv for database connection and environment variable management. One of the scripts is with raw sql, the other one is using an ORM.


![Schema](https://github.com/cberdejo/OracleSqlConnectionExample/blob/main/schema.png)

## Features
- Database Initialization: Drops existing tables and creates new ones.
- Table Structure: Sets up tables for department, employee, project, works_on, dependent, and dept_locations.
- Data Population: Inserts predefined records into the tables.
- Foreign Key Constraints: Ensures referential integrity by adding foreign key constraints.
## Setup
### 1. Install Dependencies:

Ensure Python is installed.


### 2. Install required packages:


Copiar código:
``` sh 
    `pip install -r requirements.txt`
```



### 3. Environment Variables:


Create a `.env` file based on the `env.template` file provided in the project.


#### Define the following variables:

- DB_USER=<your_db_user>
- DB_PASSWORD=<your_db_password>
- DB_HOSTNAME=<your_db_hostname>
- DB_SID=<your_db_sid>
- DB_PORT=<your_port>

### Image PostreSQL 
if needed, it is possible to use a local DB:
``` sh 
    $ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=departements -p 5432:5432 postgres

```

## Execute the script:
Use 
``` sh 
python conn.py
```
or 
``` sh 
python conn_orm.py
```

## LICENSE: MIT License file.
License
This project is licensed under the MIT License. See the LICENSE file for details.