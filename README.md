# Staff Attendance Portal

A Staff Attendance Management System built using FastAPI, SQLite and HTML/CSS.

## Features

- Add Attendance
- View Attendance
- Update Attendance
- Delete Attendance
- Search Employee
- Dashboard
- Leave Management
- Admin Login
- Export Attendance to CSV

## Technologies Used

- FastAPI
- Python
- SQLite
- HTML
- CSS
- JavaScript

## Project Structure

```
Staff-Attendance-Portal
│
├── backend
│   ├── main.py
│   ├── attendance.db
│   ├── templates
│   │   └── index.html
│
├── frontend
│   ├── src
│   └── package.json
│
└── README.md
```

## Installation

Clone the repository

```bash
git clone https://github.com/vanajapriya76-blip/Staff-Attendance-Portal.git
```

Go to backend

```bash
cd backend
```

Install requirements

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn main:app --reload
```

Open Browser

```
http://127.0.0.1:8000/frontend
```

Swagger API

```
http://127.0.0.1:8000/docs
```

## Author

Vanaja Priya
