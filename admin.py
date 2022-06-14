class Admin:

    def __init__(self):
        self.classes = list()
        self.sections = list()

    # add classes
    def add_class(self, student_class):
        self.classes.append(student_class)

    def add_section(self, section):
        self.sections.append(section)

    def add_student_to_class(self, student, student_class):


    # add sections
    # add students to classes
    # allocate staff to classes
    #


class StudentGrade:
    def __init__(self, student_class):
        self.student_class = student_class
    pass


class StudentSection:
    pass


class Student:
    def __init__(self, grade, section):
        self.grade = grade
        self.section = section
    pass


class Staff:
    pass
