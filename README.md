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
- Alembic configuration and migrations
- async SQLAlchemy session setup
- authentication and user management with FastAPI Users
- modular auth/users structure (`app/auth`, `app/users`, `app/api`)

## Project Structure

Current backend layout:

- `app/main.py` - FastAPI app entrypoint
- `app/api/routers.py` - API v1 router aggregation
- `app/api/v1/users.py` - v1 users/auth API namespace
- `app/auth/backend.py` - JWT auth backend config
- `app/auth/router.py` - auth and users routers from FastAPI Users
- `app/users/manager.py` - `UserManager` hooks and password validation
- `app/users/deps.py` - `fastapi_users` dependencies
- `app/users/schemas.py` - user schemas for auth/user endpoints
- `app/db/session.py` - async DB session and user DB adapter
- `alembic/` - migration environment and revisions

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

6. Start the app:

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

7. Open API docs:

```text
http://127.0.0.1:8000/docs
```

## Authentication Endpoints

Current auth endpoints are available under:

- `/v1/users/auth/login`
- `/v1/users/auth/register`
- `/v1/users/auth/logout`
- `/v1/users/auth/verify`
- `/v1/users/auth/request-verify-token`
- `/v1/users/auth/forgot-password`
- `/v1/users/auth/reset-password`
- `/v1/users/auth/me`

## Environment Variables

Required app settings:

- `DATABASE_URL`
- `JWT_SECRET_KEY`
- `JWT_ALG`
- `ACCESS_TOKEN_EXPIRE_SECONDS`
- `SECRET_TOKEN`
- `VERIFICATION_TOKEN_SECRET`

## Next Steps

- implement CRUD modules for `tasks` and `categories`
- add admin-only endpoints and role checks
- add service layer and repository layer for business logic
- add tests (auth, users, tasks, categories)
- add Docker profile for local development
