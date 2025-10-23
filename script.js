function login() {
  const role = document.getElementById('role').value;
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  if (!username || !password) {
    alert("Please enter both username and password.");
    return;
  }

  if (role === 'farmer') {
    window.location.href = 'farmer.html';
  } else {
    window.location.href = 'customer.html';
  }
}
