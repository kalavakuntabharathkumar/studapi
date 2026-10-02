# Student Records REST API and Reporting System

A compact Django REST Framework starter for student/staff records, filtering, reporting, and automated tests.

## Setup
```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
API root: http://127.0.0.1:8000/api/  
Admin: http://127.0.0.1:8000/admin/

## Endpoints
- `/api/students/` — list/create students
- `/api/students/{id}/` — retrieve/update/delete
- `/api/reports/summary/` — aggregate counts by grade
- `/api/health/` — health check

SQLite is used by default so the starter runs locally without external services; switch `DATABASES` to MySQL for a MySQL deployment. This is a generated starter project, not a verified reproduction of an existing production system. Any resume metrics such as API count, user count, latency, coverage, or bug count must be measured independently before being claimed.
