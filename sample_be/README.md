# Student Management System

A simple Flask backend application for managing student data with REST APIs and HTML templates.

## Setup

### 1. Install Dependencies
```bash
pip install flask
```

### 2. Initialize Database
```bash
python database.py
```

### 3. Run the Server
```bash
python app.py
```

The server will start at `http://localhost:5000`

## API Endpoints

### 1. Home Page
```
GET /
```
Interactive web page with student table and form.

### 2. Get All Students
```
GET /api/students
```
Returns all students as JSON.

**Example:**
```bash
curl http://localhost:5000/api/students
```

### 3. Filter Students by Grade
```
GET /api/students?grade=A
```
Returns students filtered by grade.

**Example:**
```bash
curl "http://localhost:5000/api/students?grade=A"
```

### 4. Get Student by ID
```
GET /api/students/<id>
```
Returns a single student by ID.

**Example:**
```bash
curl http://localhost:5000/api/students/1
```

### 5. Add New Student
```
POST /api/students
Content-Type: application/json
```
Creates a new student record.

**Example:**
```bash
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","age":20,"grade":"A","email":"john@example.com"}'
```

### 6. Server-Rendered Students View
```
GET /view/students
```
Returns an HTML page with server-side rendered student table.

## Project Structure

```
sample_be/
├── app.py              # Main Flask application
├── database.py         # Database initialization
├── requirements.txt    # Dependencies
├── static/
│   └── app.js         # Frontend JavaScript
└── templates/
    ├── index.html     # Home page
    └── students.html  # Server-rendered view
```

## Database Schema

**Table: students**
- `id` (INTEGER PRIMARY KEY)
- `name` (TEXT)
- `age` (INTEGER)
- `grade` (TEXT)
- `email` (TEXT)
