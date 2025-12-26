window.addEventListener('DOMContentLoaded', async () => {
  const token = localStorage.getItem('token');
  if (!token) {
    window.location.href = 'login.html';
    return;
  }

  // ... (Existing User Fetching Code) ... 
  // (Assuming you have fetched 'user' and 'role' as per previous code)
  
  const payload = JSON.parse(atob(token.split('.')[1]));
  const userId = payload.user_id;
  const role = payload.role;
  
  const res = await fetch(`/api/user/${userId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const user = await res.json();
  
  document.getElementById('userInfo').innerHTML = `<h1>Welcome, ${user.name}</h1><p>${role}</p>`;

  // --- Logic to Show Sections ---

  if (role === 'student') {
    document.getElementById('studentSection').style.display = 'block';
    if (typeof loadAttendance === 'function') loadAttendance(userId);
    if (typeof loadMarks === 'function') loadMarks(userId);
  }
  
  if (role === 'teacher') {
    document.getElementById('teacherSection').style.display = 'block';
    // Teachers approve Students
    loadPendingUsers('student');
  }

  if (role === 'admin') {
    // Admins approve Teachers
    loadPendingUsers('teacher');
  }

  document.getElementById('noticeSection').style.display = 'block';
  if (typeof loadNotices === 'function') loadNotices(role);
});

// --- New Approval Function ---
async function loadPendingUsers(roleToApprove) {
  const token = localStorage.getItem('token');
  const container = document.getElementById('approvalSection');
  const list = document.getElementById('pendingList');

  const res = await fetch(`/api/users/pending/${roleToApprove}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const users = await res.json();

  if (users.length > 0) {
    container.style.display = 'block';
    list.innerHTML = `
      <table style="width:100%">
        <tr><th>Name</th><th>Email</th><th>Action</th></tr>
        ${users.map(u => `
          <tr>
            <td>${u.name}</td>
            <td>${u.email}</td>
            <td>
              <button onclick="approveUser('${u._id}')" class="btn" style="padding:5px 15px; font-size:0.8em;">
                Approve
              </button>
            </td>
          </tr>
        `).join('')}
      </table>
    `;
  } else {
    // Hide section if nothing to approve
    container.style.display = 'none';
  }
}

async function approveUser(targetId) {
  const token = localStorage.getItem('token');
  if(!confirm("Confirm approval?")) return;

  const res = await fetch(`/api/users/approve/${targetId}`, {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${token}` }
  });

  if (res.ok) {
    alert("User Approved!");
    location.reload(); // Reload to refresh list
  } else {
    alert("Error approving user");
  }
}