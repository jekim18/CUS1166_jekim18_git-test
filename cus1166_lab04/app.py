from flask import Flask, render_template

app = Flask(__name__)

class_roster = [
    ('Alice A', 'A', 'Freshman'),
    ('Brittany B', 'B', 'Sophomore'),
    ('Cathy C', 'C', 'Junior'),
    ('Daffney D', 'D', 'Senior'),
    ('Evan E', 'E', 'Freshman'),
    ('Francis F', 'F', 'Senior'),
    ('Giovanni G', 'G', 'Freshman')
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

'''
@app.route("/do/i/teach/<string:course>")
def doiteach(course):
    doTeach = (course=="CUS1166") or (course=="CUS615")
    return render_template("index3.html", course=course, doTeach=doTeach)

@app.route("/roster/<string:course>")
def roster(course):
    roster = [{"John", "A"}, {"Tom", "B"}, {"Mary", "C"}, {"Lucas", "B"}]
    return

'''