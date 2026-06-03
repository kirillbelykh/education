# Education Notes Backend

## Stack

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0
- Alembic
- Pydantic
- JWT
- bcrypt

## Environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://...
SECRET_KEY=change-me
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Install dependencies

```bash
uv sync
```

## Run migrations

```bash
uv run alembic upgrade head
```

## Run server

```bash
uv run uvicorn backend.app.main:app --reload
```

## API docs

```text
http://127.0.0.1:8000/docs
```

## Main endpoints

### Auth

```text
POST   /auth/register
POST   /auth/login
GET    /auth/me
```

### Notes

```text
POST   /notes
GET    /notes
GET    /notes/trash
GET    /notes/{note_id}
PATCH  /notes/{note_id}
DELETE /notes/{note_id}
PATCH  /notes/{note_id}/restore
DELETE /notes/trash/{note_id}
```