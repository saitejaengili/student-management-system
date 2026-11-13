# Student Management System

A web-based Student Management System developed using **Python, Django, and PostgreSQL**. This application helps manage student records through a simple and user-friendly interface.

## About the Project

The Student Management System is designed to simplify student record management. It allows users to add, view, update, search, and delete student information efficiently.

## Features

- **Dashboard:** View student records in one place.
- **Add Students:** Register new student details.
- **View Students:** Display stored student information.
- **Update Students:** Edit existing student records.
- **Delete Students:** Remove unwanted student records.
- **Search Students:** Find student records easily.
- **Database Integration:** Store information using PostgreSQL.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| PostgreSQL | Database |
| HTML | Web page structure |
| CSS | Styling |
| JavaScript | Frontend interactions |
| Git & GitHub | Version control |

## Project Structure

```text
student-management-system/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   └── students/
│
├── static/
│   ├── css/
│   └── js/
│
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/saitejaengili/student-management-system.git
```

### 2. Open the Project Folder

```bash
cd student-management-system
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure PostgreSQL

- Install and open PostgreSQL.
- Create a database named `student_management_db`.
- Copy `.env.example` and rename the copy to `.env`.
- Update the database credentials in your local `.env` file.

Example configuration:

```env
DB_NAME=student_management_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

**Note:** Never upload your actual `.env` file or database password to GitHub.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Start the Development Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

## Screenshots

Add screenshots of your application here to demonstrate the dashboard and student management features.

Suggested images:

- Dashboard
- Add Student Page
- Student Records
- Search Results

## Future Enhancements

- Student authentication and role-based access.
- Export student records to Excel or PDF.
- Attendance management.
- Improved dashboard analytics.

## Author

**Sai Teja**

Computer Science Student

GitHub: [saitejaengili](https://github.com/saitejaengili)

## License

This project is available for educational and learning purposes.