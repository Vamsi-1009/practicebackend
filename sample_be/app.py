from flask import Flask, render_template, request, jsonify
import sqlite3
from database import init_db

app = Flask(__name__)

# Initialize database on startup
init_db()

def get_db_connection():
    """Helper function to get database connection"""
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row  # Returns rows as dictionaries
    return conn

# Route 1: Home page (HTML)
@app.route('/')
def home():
    return render_template('index.html')

# Route 2: Get all students with optional grade filter (JSON)
@app.route('/api/students', methods=['GET'])
def get_students():
    grade_filter = request.args.get('grade')
    conn = get_db_connection()

    if grade_filter:
        students = conn.execute(
            'SELECT * FROM students WHERE grade = ?',
            (grade_filter,)
        ).fetchall()
    else:
        students = conn.execute('SELECT * FROM students').fetchall()

    conn.close()

    students_list = [dict(student) for student in students]
    return jsonify(students_list)

# Route 3: Add new student (JSON body)
@app.route('/api/students', methods=['POST'])
def add_student():
    data = request.get_json()

    # Validate required fields
    required_fields = ['name', 'age', 'grade', 'email']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f"Missing required field: {field}"}), 400

    # Insert into database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)',
        (data['name'], data['age'], data['grade'], data['email'])
    )
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()

    return jsonify({
        'message': 'Student added successfully',
        'id': student_id
    }), 201

# Route 4: Get student by ID (JSON)
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    conn = get_db_connection()
    student = conn.execute(
        'SELECT * FROM students WHERE id = ?',
        (student_id,)
    ).fetchone()
    conn.close()

    if student is None:
        return jsonify({'error': 'Student not found'}), 404

    return jsonify(dict(student))

# Route 5: View students page (HTML with server-side rendering)
@app.route('/view/students')
def view_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()

    return render_template('students.html', students=students)

if __name__ == '__main__':
    print("=" * 50)
    print("Starting Flask server...")
    print("Server will run on http://localhost:5000")
    print("Access from network: http://<your-ip>:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
