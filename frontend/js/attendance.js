async function loadAttendance(studentId) {
    const token = localStorage.getItem('token');
    const res = await fetch(`/api/attendance/${studentId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
    });
    const data = await res.json();
    
    const container = document.getElementById('attendanceData');
    if (data.length === 0) {
        container.innerHTML = '<p>No attendance records found.</p>';
        return;
    }

    const html = `
        <table border="1">
            <tr><th>Date</th><th>Status</th></tr>
            ${data.map(record => `<tr><td>${record.date}</td><td>${record.status}</td></tr>`).join('')}
        </table>
    `;
    container.innerHTML = html;
}

// Handle Teacher Marking Attendance
const markForm = document.getElementById('markAttendanceForm');
if (markForm) {
    markForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const token = localStorage.getItem('token');
        const student_id = document.getElementById('studentId').value;
        const date = document.getElementById('date').value;
        const status = document.getElementById('status').value;

        const res = await fetch('/api/attendance', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ student_id, date, status })
        });

        if (res.ok) {
            alert('Attendance marked successfully');
        } else {
            alert('Error marking attendance');
        }
    });
}