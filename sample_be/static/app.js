// Load all students from API
function loadStudents() {
    fetch('/api/students')
        .then(response => response.json())
        .then(data => displayStudents(data))
        .catch(error => {
            console.error('ERROR in fetch:', error);
            showMessage('Error loading students: ' + error.message, 'error');
        });
}

// Load students filtered by grade A
function loadStudentsByGrade() {
    const grade = 'A';
    fetch('/api/students?grade=' + grade)
        .then(response => response.json())
        .then(data => displayStudents(data))
        .catch(error => {
            console.error('ERROR in fetch:', error);
            showMessage('Error loading students: ' + error.message, 'error');
        });
}

// Display students in table
function displayStudents(students) {
    const tableBody = document.getElementById('tableBody');
    tableBody.innerHTML = '';

    students.forEach((student) => {
        const row = document.createElement('tr');
        row.innerHTML = '<td>' + student.id + '</td>' +
                       '<td>' + student.name + '</td>' +
                       '<td>' + student.age + '</td>' +
                       '<td>' + student.grade + '</td>' +
                       '<td>' + student.email + '</td>';
        tableBody.appendChild(row);
    });

    showMessage('Loaded ' + students.length + ' students', 'success');
}

// Add new student
function addStudent() {
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const grade = document.getElementById('grade').value;
    const email = document.getElementById('email').value;

    if (!name || !age || !grade || !email) {
        showAddMessage('Please fill all fields', 'error');
        return;
    }

    const studentData = {
        name: name,
        age: parseInt(age),
        grade: grade,
        email: email
    };

    fetch('/api/students', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(studentData)
    })
    .then(response => response.json())
    .then(data => {
        showAddMessage('Student added! ID: ' + data.id, 'success');
        document.getElementById('name').value = '';
        document.getElementById('age').value = '';
        document.getElementById('grade').value = '';
        document.getElementById('email').value = '';
        loadStudents();
    })
    .catch(error => {
        console.error('ERROR in POST request:', error);
        showAddMessage('Error adding student: ' + error.message, 'error');
    });
}

// Helper function to show messages
function showMessage(msg, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = msg;
    messageDiv.className = type;
}

function showAddMessage(msg, type) {
    const messageDiv = document.getElementById('addMessage');
    messageDiv.textContent = msg;
    messageDiv.className = type;
}
