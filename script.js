// Login logic
function login() {
  const role = document.getElementById('role').value;
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  if (!username || !password) {
    alert("Please enter both username and password.");
    return;
  }

  // Simulate login (replace with real auth later)
  if (role === 'farmer') {
    window.location.href = 'farmer.html';
  } else {
    window.location.href = 'customer.html';
  }
}

// Show dashboard sections
function showSection(id) {
  document.querySelectorAll('section').forEach(sec => sec.classList.add('hidden'));
  document.getElementById(id).classList.remove('hidden');
}

// Toggle registration form
function toggleForm() {
  const type = document.getElementById('userType').value;
  document.getElementById('farmerForm').classList.toggle('hidden', type !== 'farmer');
  document.getElementById('customerForm').classList.toggle('hidden', type !== 'customer');
}

// Farmer registration (mocked)
document.getElementById('farmerForm')?.addEventListener('submit', function (e) {
  e.preventDefault();
  alert("Farmer registered successfully!");
  window.location.href = 'index.html';
});

// Customer registration (mocked)
document.getElementById('customerForm')?.addEventListener('submit', function (e) {
  e.preventDefault();
  alert("Customer registered successfully!");
  window.location.href = 'index.html';
});
