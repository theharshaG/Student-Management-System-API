from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# -------------------------
# DATABASE CONFIG
# -------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------
# MODEL
# -------------------------
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

# -------------------------
# CREATE DB
# -------------------------
with app.app_context():
    db.create_all()

# -------------------------
# HOME
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------------
# ADD
# -------------------------
@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()

    student = Student(name=data["name"], age=data["age"])
    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Student added"})

# -------------------------
# GET ALL
# -------------------------
@app.route("/students")
def get_students():
    students = Student.query.all()

    result = []
    for s in students:
        result.append({
            "id": s.id,
            "name": s.name,
            "age": s.age
        })

    return jsonify(result)

# -------------------------
# UPDATE
# -------------------------
@app.route("/update/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()

    student = Student.query.get(id)
    student.name = data["name"]
    student.age = data["age"]

    db.session.commit()

    return jsonify({"message": "Updated"})

# -------------------------
# DELETE
# -------------------------
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    student = Student.query.get(id)

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Deleted"})

# -------------------------
# SEARCH
# -------------------------
@app.route("/search")
def search():
    name = request.args.get("name")

    students = Student.query.filter(
        Student.name.like(f"%{name}%")
    ).all()

    result = []
    for s in students:
        result.append({
            "id": s.id,
            "name": s.name,
            "age": s.age
        })

    return jsonify(result)

# -------------------------
# FILTER
# -------------------------
@app.route("/filter")
def filter_age():
    age = request.args.get("age")

    students = Student.query.filter_by(age=age).all()

    result = []
    for s in students:
        result.append({
            "id": s.id,
            "name": s.name,
            "age": s.age
        })

    return jsonify(result)

# -------------------------
# COUNT
# -------------------------
@app.route("/count")
def count():
    total = Student.query.count()
    return jsonify({"total": total})

# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
