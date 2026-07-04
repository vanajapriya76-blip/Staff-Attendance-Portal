from fastapi import FastAPI,Form
from fastapi.responses import FileResponse, HTMLResponse
import sqlite3
import csv

app = FastAPI()

# create table
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

# home
@app.get("/")
def home():
    return {"message": "Server running"}

# add attendance
@app.post("/attendance")
def add_attendance(name: str, date: str, status: str):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attendance (name, date, status) VALUES (?, ?, ?)",
        (name, date, status)
    )

    conn.commit()
    conn.close()

    return {"message": "Attendance added"}

# view attendance
@app.get("/view")
def view():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")

    data = cursor.fetchall()

    conn.close()

    return {"data": data}

from fastapi import FastAPI
import sqlite3

app = FastAPI()

# create table
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    status TEXT
)
""")

# NEW LEAVE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS leave_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT,
    reason TEXT,
    from_date TEXT,
    to_date TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

# home
@app.get("/")
def home():
    return {"message": "Server running"}

# add attendance
@app.post("/attendance")
def add_attendance(
    name: str = Form(...),
    date: str = Form(...),
    status: str = Form(...)
):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attendance (name, date, status) VALUES (?, ?, ?)",
        (name, date, status)
    )

    conn.commit()
    conn.close()

    return {"message": "Attendance added"}

# view attendance
@app.get("/view")
def view():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")

    data = cursor.fetchall()

    conn.close()

    return {"data": data}

# APPLY LEAVE
@app.post("/leave")
def apply_leave(
    employee_name: str,
    reason: str,
    from_date: str,
    to_date: str
):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO leave_requests
        (employee_name, reason, from_date, to_date, status)

        VALUES (?, ?, ?, ?, ?)
        """,
        (employee_name, reason, from_date, to_date, "Pending")
    )

    conn.commit()
    conn.close()

    return {"message": "Leave Applied"}

# VIEW LEAVE REQUESTS
@app.get("/leave")
def view_leave():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leave_requests")

    data = cursor.fetchall()

    conn.close()

    return {"leave_data": data}

# APPROVE LEAVE
@app.put("/approve/{id}")
def approve_leave(id: int):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE leave_requests SET status = ? WHERE id = ?",
        ("Approved", id)
    )

    conn.commit()
    conn.close()

    return {"message": "Leave Approved"}

# REJECT LEAVE
@app.put("/reject/{id}")
def reject_leave(id: int):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE leave_requests SET status = ? WHERE id = ?",
        ("Rejected", id)
    )

    conn.commit()
    conn.close()

    return {"message": "Leave Rejected"}

    # DASHBOARD
@app.get("/dashboard")
def dashboard():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # total attendance records
    cursor.execute("SELECT COUNT(*) FROM attendance")
    total = cursor.fetchone()[0]

    # present count
    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE status='Present'"
    )
    present = cursor.fetchone()[0]

    # absent count
    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE status='Absent'"
    )
    absent = cursor.fetchone()[0]

    # leave count
    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE status='Leave'"
    )
    leave = cursor.fetchone()[0]

    conn.close()

    return {
        "total_records": total,
        "present": present,
        "absent": absent,
        "leave": leave
    }

    # UPDATE ATTENDANCE
@app.put("/update/{id}")
def update_attendance(
    id: int,
    name: str,
    date: str,
    status: str
):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE attendance
        SET name = ?, date = ?, status = ?
        WHERE id = ?
        """,
        (name, date, status, id)
    )

    conn.commit()
    conn.close()

    return {"message": "Attendance Updated"}

    # DELETE ATTENDANCE
@app.delete("/delete/{id}")
def delete_attendance(id: int):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM attendance WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Attendance Deleted"}

    # SEARCH EMPLOYEE
@app.get("/search/{name}")
def search_employee(name: str):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM attendance WHERE name = ?",
        (name,)
    )

    data = cursor.fetchall()

    conn.close()

    return {"search_result": data}

# LOGIN
@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):

    if username == "admin" and password == "admin123":
        return {"message": "Login Success"}

    else:
        return {"message": "Invalid Username or Password"}

# EXPORT CSV
@app.get("/export")
def export_csv():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")

    data = cursor.fetchall()

    conn.close()

    file_name = "attendance_report.csv"

    with open(file_name, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Date", "Status"]
        )

        writer.writerows(data)

    return FileResponse(
        path=file_name,
        media_type='text/csv',
        filename=file_name
    )

# FRONTEND PAGE
@app.get("/frontend")
def frontend():
    return FileResponse("index.html")
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # attendance table data
    cursor.execute("SELECT * FROM attendance")
    data = cursor.fetchall()

    # dashboard data
    cursor.execute("SELECT COUNT(*) FROM attendance")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE status='Present'"
    )
    present = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE status='Absent'"
    )
    absent = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE status='Leave'"
    )
    leave = cursor.fetchone()[0]

    conn.close()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "data": data,
            "total": total,
            "present": present,
            "absent": absent,
            "leave": leave
        }
    )
    
@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):

    if username == "admin" and password == "admin123":
        return {"message": "Login Success"}

    else:
        return {"message": "Invalid Username or Password"}

@app.get("/dashboard-ui", response_class=HTMLResponse)
def dashboard_ui():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM attendance")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE status='Present'"
    )
    present = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE status='Absent'"
    )
    absent = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE status='Leave'"
    )
    leave = cursor.fetchone()[0]

    conn.close()

    html = f'''

    <html>

    <head>

    <title>Dashboard</title>

    <style>

    body{{
        font-family: Arial;
        background:#f2f2f2;
        padding:20px;
    }}

    h1{{
        text-align:center;
        color:blue;
    }}

    .container{{
        display:flex;
        gap:20px;
        justify-content:center;
        margin-top:50px;
    }}

    .card{{
        background:white;
        padding:30px;
        width:200px;
        text-align:center;
        border-radius:10px;
        box-shadow:0px 0px 10px gray;
    }}

    </style>

    </head>

    <body>

    <h1>Attendance Dashboard</h1>

    <div class="container">

        <div class="card">
            <h2>Total</h2>
            <h3>{total}</h3>
        </div>

        <div class="card">
            <h2>Present</h2>
            <h3>{present}</h3>
        </div>

        <div class="card">
            <h2>Absent</h2>
            <h3>{absent}</h3>
        </div>

        <div class="card">
            <h2>Leave</h2>
            <h3>{leave}</h3>
        </div>

    </div>

    </body>
    </html>

    '''

    return html

@app.get("/export")
def export_csv():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")

    data = cursor.fetchall()

    conn.close()

    file_name = "attendance_report.csv"

    with open(file_name, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Date", "Status"]
        )

        writer.writerows(data)

    return FileResponse(
        path=file_name,
        media_type='text/csv',
        filename=file_name
    )

    
