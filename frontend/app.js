import { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [status, setStatus] = useState("");

  const submitAttendance = async () => {
    await fetch(
      `http://127.0.0.1:8000/attendance?name=${name}&status=${status}&date=2026-05-07`,
      {
        method: "POST",
      }
    );

    alert("Attendance Added");
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>Staff Attendance Portal</h1>

      <input
        placeholder="Employee Name"
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="Status"
        onChange={(e) => setStatus(e.target.value)}
      />

      <br /><br />

      <button onClick={submitAttendance}>
        Submit Attendance
      </button>
    </div>
  );
}

