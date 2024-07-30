# Semaphore API

## Work Notes
- ...

## Environment
- Python 3.10.11
- MariaDB 10.4

## Clone the Project
To clone this project, run the following command:
```sh
git clone https://github.com/isnandar1471/semaphore-api.git
```

## Install Dependencies
To install all necessary dependencies, run:
```sh
pip install -r requirements.txt
```

Important dependencies:
- `tensorflow`: For reading imported models.
- `bcrypt`: For password encryption.
- `sqlalchemy`: For ORM.
- `sqlalchemy-seeder`: For seeding.
- `alembic`: For database version control.
- `fastapi`: For REST API.
- `starlette`: For ASGI framework.
- `uvicorn`: For ASGI server.
- `python-dotenv`: For reading env files.
- `pymysql`: For MySQL connection.
- `pydantic`: For data validation.
- `pyjwt`: For generating JWT.
- `pillow`: For image processing.
- `numpy`: For image conversion.

## Error Documentation
- `sqlalchemy` requires `pymysql`, but it is not automatically installed.
- Some dependencies require `pillow`.

## Copy `.env.example` to `.env`, and change the value to what you need
```shell
cp .env.example .env
```

## Token
Using JWT for authentication.

## Database

### Migrations
To create a new migration:
```sh
alembic revision -m "<migration_description>"
```

To run migrations up to a specific version:
```sh
alembic upgrade <version>
```

To run migrations to the latest version:
```sh
alembic upgrade head
```

To rollback x number of migrations:
```sh
alembic downgrade <-x>
```

### Seeding
To seed the database, run the following command:
```sh
python -m src.seeder.seeder
```

## Running the Application
To run the application, use:
```sh
python main.py
```

## Running the Application with Docker
This application can also be run in Docker using the provided scripts in the docker folder.

## Additional Resources

### Installing All Packages from requirements.txt
A guide for installing all available packages from requirements.txt can be found [here](https://stackoverflow.com/questions/35802939/install-only-available-packages-using-conda-install-yes-file-requirements-t).

### Using AutoFlake to Remove Unused Imports
```sh
autoflake --in-place --remove-all-unused-imports <filepath>
```

### Using isort to Sort Import Statements
```sh
isort <filepath>
```

## Linter Using pylint
To maintain code quality, use pylint as a linter.