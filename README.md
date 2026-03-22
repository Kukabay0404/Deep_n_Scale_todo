# Deep_n_Scale To-Do

A backend foundation for a To-Do application built with FastAPI, SQLAlchemy, Alembic, and PostgreSQL.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL

## Project Status

Current progress:

- database models for `User`, `Task`, and `Category`
- Alembic configuration and initial migration
- async SQLAlchemy session setup

## Local Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create your local environment file:

```bash
copy .env.example .env
```

4. Update `.env` with your local database settings.
5. Run migrations:

```bash
alembic upgrade head
```

## Next Steps

- add Pydantic schemas
- build CRUD endpoints
- implement authentication
- add Docker support
- add tests
