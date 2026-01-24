from flask import Flask, request, redirect

app = Flask(__name__)

students = []

def grade(m):
    if m >= 85:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 50:
        return "C"
    return "F"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        marks = float(request.form["marks"])

        students.append({
            "name": name,
            "course": course,
            "marks": marks,
            "grade": grade(marks)
        })
        return redirect("/")

    html = """
    <h2>Students</h2>
    <form method="post">
        <input name="name" placeholder="Name">
        <input name="course" placeholder="Course">
        <input name="marks" placeholder="Marks">
        <button>Add</button>
    </form>
    <ul>
    """
    for s in students:
        html += f"<li>{s['name']} | {s['course']} | {s['marks']} | {s['grade']}</li>"
    html += "</ul>"

    return html

app.run()
