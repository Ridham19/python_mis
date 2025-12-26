async function loadNotices(role) {
    const token = localStorage.getItem('token');
    const res = await fetch(`/api/notice/${role}`, {
        headers: { 'Authorization': `Bearer ${token}` }
    });
    const data = await res.json();
    
    const container = document.getElementById('notices');
    if (data.length === 0) {
        container.innerHTML = '<p>No notices.</p>';
        return;
    }

    container.innerHTML = data.map(n => `
        <div class="notice-card" style="border:1px solid #ccc; margin: 10px; padding: 10px;">
            <h4>${n.title}</h4>
            <p>${n.content}</p>
        </div>
    `).join('');
}