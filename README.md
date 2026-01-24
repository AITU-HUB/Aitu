# AITU Hub

University platform with Django (web + auth + admin) and FastAPI (REST API) using a shared database.

## Modules
- Lost & Found
- Buy & Sell
- AITU News

## Tech
- Django 5 + Django Admin + session auth for web pages
- JWT for API auth (issued by Django, validated by FastAPI)
- FastAPI for REST endpoints
- PostgreSQL (Docker) or SQLite (local dev)

## Quick Start (Docker)
1) Copy env file:
```bash
cp .env.example .env
```
2) Start services:
```bash
docker compose up --build
```
3) Run migrations + seed data:
```bash
docker compose exec backend_django python manage.py migrate

docker compose exec backend_django python manage.py seed_data
```

Web UI: http://localhost:8000/
FastAPI docs: http://localhost:8001/docs
Django admin: http://localhost:8000/admin/

Seeded users:
- Admin: `admin@aitu.local` / `admin123`
- User: `user@aitu.local` / `user123`

## JWT Auth Flow
1) Get token from Django:
```bash
POST http://localhost:8000/auth/login/
{
  "email": "user@aitu.local",
  "password": "user123"
}
```
Response contains `access` and `refresh`.

2) Use token in FastAPI:
```
Authorization: Bearer <access>
```

## API Endpoints
Lost & Found:
- `GET /api/lostfound?status=lost|found`
- `GET /api/lostfound/{id}`
- `POST /api/lostfound` (auth required)
- `PUT /api/lostfound/{id}` (owner only)
- `DELETE /api/lostfound/{id}` (owner or admin)

Buy & Sell:
- `GET /api/products?category=electronics|books|furniture|others`
- `GET /api/products/{id}`
- `POST /api/products` (auth required)
- `PUT /api/products/{id}` (owner only)
- `DELETE /api/products/{id}` (owner or admin)

News:
- `GET /api/news`
- `GET /api/news/{id}`
- `POST /api/news` (admin only)
- `PUT /api/news/{id}` (admin only)
- `DELETE /api/news/{id}` (admin only)

Health:
- `GET /api/health`

## Local Dev (without Docker)
1) Django:
```bash
cd backend_django
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver 8000
```

2) FastAPI:
```bash
cd api_fastapi
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

If you use SQLite locally, set:
```
DATABASE_URL=sqlite:///./backend_django/db.sqlite3
```