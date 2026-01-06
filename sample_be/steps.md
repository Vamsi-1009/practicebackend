# API Routes - 5 Endpoints

## Debugging Goal

**Objective:** Learn how backend routing and database operations work by debugging each API endpoint.

**Steps:**
1. Add `breakpoint()` or `import pdb; pdb.set_trace()` in all 5 route functions in `app.py`:
   - Line 19 in `home()`
   - Line 24 in `get_students()`
   - Line 43 in `add_student()`
   - Line 70 in `get_student_by_id()`
   - Line 85 in `view_students()`

2. Run `app.py` in command-line debug mode:
   ```bash
   python -m pdb app.py
   ```

3. In another terminal, trigger each API endpoint using curl commands below

4. When breakpoint hits in the debugger:
   - Type `w` or `where` to examine the **call stack**
   - Type `s` to **step into** database functions (`conn.execute()`)
   - Type `p variable_name` to inspect: `request.args`, `request.get_json()`, `students`, `student_id`
   - Type `c` to continue to next breakpoint
   - Type `q` to quit debugger

5. Observe:
   - How query parameters are extracted (`request.args.get()`)
   - How JSON request body is parsed (`request.get_json()`)
   - How database queries execute and return data
   - How responses are created (`jsonify()`, `render_template()`)

---

## 1. GET / - Home Page
- **Type:** HTML response
- **Purpose:** Serves the interactive home page with student table and form
- **Access:** `http://localhost:5000/`

**Sample curl commands:**
```bash
# Get the home page HTML
curl http://localhost:5000/

# Get home page and show only first 20 lines
curl http://localhost:5000/ | head -20
```

## 2. GET /api/students - Get All Students (with optional filter)
- **Type:** JSON API
- **Purpose:** Returns all students or filters by grade using query parameter
- **Response:** JSON array of student objects

**Sample curl commands:**
```bash
# Get all students
curl http://localhost:5000/api/students

# Get only grade A students (use quotes for query parameters)
curl "http://localhost:5000/api/students?grade=A"
```

## 3. POST /api/students - Add New Student
- **Type:** JSON API
- **Purpose:** Creates a new student record
- **Required fields:** name, age, grade, email
- **Response:** `{"message": "Student added successfully", "id": <new_id>}`

**Sample curl commands:**
```bash
# Add a new student with all required fields
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Priya Sharma","age":21,"grade":"A","email":"priya@example.com"}'

# Add another student
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Rahul Verma","age":22,"grade":"B","email":"rahul@example.com"}'
```

## 4. GET /api/students/<id> - Get Student by ID
- **Type:** JSON API
- **Purpose:** Returns a specific student by their ID
- **Response:** JSON object with student data or 404 error if not found

**Sample curl commands:**
```bash
# Get student with ID 1
curl http://localhost:5000/api/students/1

# Get student with ID 5
curl http://localhost:5000/api/students/5
```

## 5. GET /view/students - Server-Rendered Students View
- **Type:** HTML response (server-side rendering)
- **Purpose:** Returns an HTML table of all students using Jinja2 templates
- **Note:** Demonstrates server-side rendering vs client-side rendering

**Sample curl commands:**
```bash
# Get the server-rendered HTML page
curl http://localhost:5000/view/students

# Get the page and extract only table rows
curl http://localhost:5000/view/students | grep "<tr>"
```

---

## Key Concepts Demonstrated
- **JSON APIs:** Routes 2, 3, and 4
- **Query Parameters:** Route 2 (`?grade=A`)
- **Path Parameters:** Route 4 (`/<id>`)
- **HTML Rendering:** Routes 1 and 5
- **HTTP Methods:** GET and POST
- **Database Operations:** All routes interact with SQLite database
