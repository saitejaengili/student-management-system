# Student Management System

A beginner-friendly Student Management System built with Python, Django, PostgreSQL, HTML, CSS and JavaScript.

## Features
- Dashboard with total student count
- Create, view, update and delete student records
- Search by name, roll number, email or department
- Responsive layout
- Server-side form validation

## 1. Create and activate a virtual environment (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once in the current terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 2. Install dependencies

```powershell
pip install -r requirements.txt
```

## 3. Configure PostgreSQL

Create a database named `student_management_db` in pgAdmin 4:
1. Open pgAdmin and connect to your PostgreSQL 18 server.
2. Right-click Databases -> Create -> Database.
3. Enter `student_management_db` and save.

Copy `.env.example` to `.env` and enter your PostgreSQL password.

## 4. Run migrations and start the server

```powershell
python manage.py makemigrations students
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## 5. Push to GitHub

Create an empty repository on GitHub, then run these commands from this project folder:

```powershell
git init
git add .
git commit -m "Build Student Management System with Django"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your actual GitHub repository URL. Do not commit your `.env` file or share your database password.

## Notes
- The app uses Django's built-in development server. Do not use it as a production server.
- Change `SECRET_KEY` and set `DEBUG=False` before any real deployment.
