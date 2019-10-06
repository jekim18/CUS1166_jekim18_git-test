# Import appropriate libraries,
import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# This module defines that database parameters.
from config import Config
# Load the models (i.e. Flights, Passenger model classes)
from models import *

# Define an instance of flask application, load database parameters.
app = Flask(__name__)
app.config.from_object(Config)
# SQLAlchemy class need an instance of the flask app to know of the application model.
db.init_app(app)


# Define a route
@app.route("/")
def index():
    # Equivalent to: "SELECT * from flights" SQL statement.
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route("/add_course", methods=["post"])
def add_course():
    id = request.form.get("id")
    course_number = request.form.get("course_number")
    course_title = request.form.get("course_title")
    course = Course(id=id, course_number=course_number, course_title=course_title)
    db.session.add(course)
    db.session.commit()
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route("/register_student/<int:course_id>", methods=['POST','GET'])
def register_student(course_id):
    course = Course.query.get(course_id)
    if request.method == 'GET':
        return render_template('course_details.html', course=course)
    elif request.method == 'POST':
        id = request.form.get("id")
        name = request.form.get('name')
        grade = request.form.get('grade')
        # Check if ID already exists
        if(RegisteredStudent.query.get(id)):
            # If the id already exists, simply add the student with that id to the course.
            student = RegisteredStudent.query.get(id)
            course.students.append(student)
        else:
            student = RegisteredStudent(id=id, name=name, grade=grade)
            course.students.append(student)
            db.session.add(student)
            db.session.commit()
        return render_template('course_details.html', course=course)

def main():
    if len(sys.argv) == 2:
        print(sys.argv)
    if sys.argv[1] == 'createdb':
        db.create_all()
    else:
        print("Run app using 'flask run'")
        print("To create a database use 'python app.py createdb")
        # Run the main method in the context of our flask application
        # This allows db know about our models.
if __name__ == "__main__":
    with app.app_context():
        main()