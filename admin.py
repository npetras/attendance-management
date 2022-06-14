import itertools
from string import ascii_lowercase

class FullSection(Exception):
    pass




class Student:
    id_iter = itertools.count(1)
    def __init__(self, name):
        self.id = next(self.id_iter)
        self.name = name


class Staff:
    pass


class Admin:

    def __init__(self):
        
        self.data = {}


    # add classes
    def add_grade(self, grade: int):
        if (grade in self.data):
            print("Grade already exists")
        else:
            self.data[grade] = {"No of students": 0, "Max": 20, "Num sections": 0, "Sections": {}}


    def add_section(self, grade: int, section: str):
        if (section in self.data[grade]["Sections"]):
            print("Section already exists")
        else:
            self.data[grade]["Sections"][section] = []
            self.data[grade]["Num sections"] += 1


    def add_student_to_class(self, student: Student, grade: int, section: str):
        try:
            if (len(self.data[grade]["Sections"][section]) >= self.data[grade]["Max"]):
                raise FullSection("Section is full, add student to another section or create a new section")
            self.data[grade]["Sections"][section].append(student)
            self.data[grade]["No of students"] += 1
        except FullSection as a:
            print(a)
            return

    # add sections
    # add students to classes
    # allocate staff to classes
    #

a = Admin()
a.add_grade(1)
a.add_grade(2)
a.add_grade(3)
a.add_grade(4)
a.add_section(1, 'a')
a.add_section(1, 'b')
a.add_section(1, 'c')
a.add_section(2, 'a')
a.add_section(2, 'b')
a.add_section(3, 'b')
a.add_section(3, 'b')
jeff = Student('Jeff')
a.add_student_to_class(jeff, 2, 'b')
print(a.data)

