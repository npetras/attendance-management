import itertools
from string import ascii_lowercase


class Grade:
    max_students_per_section = 20

    def __init__(self):
        self.sections = list()

    def add_section(self, section):
        self.sections.append(section)


class GradeSection:
    id_iter = itertools.count(1)

    def __init__(self, grade, staff):
        self.section_id = next(self.id_iter)
        self.grade = grade
        self.students = list()
        self.staff = staff

    def add_student(self, student):
        self.students.append(student)

    def display(self):
        pass
        # print(section)


class Student:
    id_iter = itertools.count(1)

    def __init__(self, name):
        self.id = next(self.id_iter)
        self.name = name


class Staff:
    pass


class Admin:

    def __init__(self):
        self.grades = list()

    # add classes
    def add_grade(self, grade):
        print("Adding grade")
        self.grades.append(Grade())

    def add_section(self, grade):
        print("Adding section")
        # grade_filter = filter(lambda student: if )

    def add_student_to_class(self, student, student_class):
        pass

    # add sections
    # add students to classes
    # allocate staff to classes
    #
