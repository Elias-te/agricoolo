function login() {
  const role = document.getElementById('role').value;
  if (role === 'farmer') {
    window.location.href = 'farmer.html';
  } else {
    window.location.href = 'customer.html';
  }
}

function showSection(id) {
  document.querySelectorAll('section').forEach(sec => sec.classList.add('hidden'));
  document.getElementById(id).classList.remove('hidden');
}
