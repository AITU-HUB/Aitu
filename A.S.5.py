import sqlite3

DB_NAME = "students.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        marks REAL,
        grade TEXT
    )
    """)

    conn.commit()
    conn.close()

def view_students():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    conn.close()

    if not rows:
        print("No students found")
        return

    for r in rows:
        print(r)


def calc_grade(m):
    if m >= 85:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 50:
        return "C"
    else:
        return "F"
    

def add_student():
    name = input("Enter name: ")
    course = input("Enter course: ")

    try:
        marks = float(input("Enter marks: "))
    except:
        print("Marks must be a number")
        return

    grade = calc_grade(marks)

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, course, marks, grade) VALUES (?, ?, ?, ?)",
        (name, course, marks, grade)
    )
    conn.commit()
    conn.close()

    print("Student added successfully")
def update_student_marks():
    try:
        student_id = int(input("Enter student ID: "))
        new_marks = float(input("Enter new marks: "))
    except:
        print("Invalid input")
        return

    new_grade = calc_grade(new_marks)

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE students SET marks=?, grade=? WHERE student_id=?",
        (new_marks, new_grade, student_id)
    )

    if cur.rowcount == 0:
        print("Student not found")
    else:
        print("Student updated successfully")
    
    conn.commit()
    conn.close()

def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
    except:
        print("Invalid input")
        return

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM students WHERE student_id=?",
        (student_id,)
    )

    if cur.rowcount == 0:
        print("Student not found")
    else:
        print("Student deleted successfully")

    conn.commit()
    conn.close()

def search_students():
    query = input("Enter name or course to search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM students WHERE name LIKE ? OR course LIKE ?",
        (f"%{query}%", f"%{query}%")
    )

    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No matching students found")
        return

    for r in rows:
        print(r)

def menu():
    while True:
        print("""
A. Add Student
B. View Students
C. Update Student Marks
D. Delete Student
E. Search Student
F. Exit
""")

        choice = input("Choose option: ").upper()

        if choice == "A":
            add_student()
        elif choice == "B":
            view_students()
        elif choice == "C":
            update_student_marks()
        elif choice == "D":
            delete_student()
        elif choice == "E":
            search_students()
        elif choice == "F":
            print("Bye")
            break
        else:
            print("Invalid option")


create_table()
menu()
