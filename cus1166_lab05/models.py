from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class RegisteredStudent(db.Model):
    __tablename__ = 'registeredstudent'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    grade = db.Column(db.Integer)
    courses = db.relationship('Course', secondary='link')


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String)
    course_title = db.Column(db.String)
    students = db.relationship('RegisteredStudent', secondary='link')

class Link(db.Model):
   __tablename__ = 'link'
   registeredstudent_id = db.Column(
      db.Integer,
      db.ForeignKey('registeredstudent.id'),
      primary_key=True)

   course_id = db.Column(
       db.Integer,
       db.ForeignKey('course.id'),
       primary_key=True)

'''
class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String, nullable=False)
    course_title = db.Column(db.String, nullable=False)
    students = db.relationship('RegisteredStudent', secondary='studentcourses')

class RegisteredStudent(db.Model):
    __tablename__ = "registeredstudents"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    courses = db.relationship('Course', secondary='studentcourses')

class StudentCourses(db.Model):
    __tablename__ = 'studentcourses'
    student_id = db.Column(
        db.Integer,
        db.ForeignKey('registeredstudents.id'),
        primary_key=True)
    course_id = db.Column(
        db.Integer,
        db.ForeignKey('courses.id'),
        primary_key=True)
'''