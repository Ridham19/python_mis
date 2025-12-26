async function loadMarks(studentId) {
    const token = localStorage.getItem('token');
    const res = await fetch(`/api/marks/${studentId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
    });
    const data = await res.json();
    
    const container = document.getElementById('marksData');
    if (data.length === 0) {
        container.innerHTML = '<p>No marks found.</p>';
        return;
    }

    const html = `
        <table border="1">
            <tr><th>Subject</th><th>Score</th></tr>
            ${data.map(m => `<tr><td>${m.subject}</td><td>${m.score}</td></tr>`).join('')}
        </table>
    `;
    container.innerHTML = html;
}