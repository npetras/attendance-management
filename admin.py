import itertools
from string import ascii_lowercase

class Grade:
    max_students_per_section = 20
    def __init__(self):
        self.sections = list()

    def add_section(self, section):
        self.sections.append(section)


class GradeSection:
    def __init__(self, grade, staff):
        # FIXME: add auto alphabetical ids
        self.section_id  = None
        self.grade = grade
        self.students = list()
        self.staff = staff


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
        self.grades.append(Grade())

    def add_section(self, grade):
        grade_filter = filter(lambda student: if )


    def add_student_to_class(self, student, student_class):


    # add sections
    # add students to classes
    # allocate staff to classes
    #



