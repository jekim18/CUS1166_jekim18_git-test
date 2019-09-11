from mymodules.models import Student
from mymodules.math_utils import average_grade
if __name__ == '__main__':
    student_list = [
        Student("John",98.0),
        Student("Matt", 100.0),
        Student("Andy", 96.0),
        Student("Bob", 91.0),
        Student("Cathy", 67.0),
        Student("Johny", 98.0),
        Student("Matty", 100.0),
        Student("Andyy", 96.0),
        Student("Boby", 91.0),
        Student("Cathyy", 67.0)
    ]
    for i in student_list:
        i.print_student_info()
    print("Their average is: " + str(average_grade(student_list)))