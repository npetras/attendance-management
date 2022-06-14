import itertools
from string import ascii_lowercase


class FullSection(Exception):
    pass


studentLookup = {}

class Student:
    id_iter = itertools.count(1)
    def __init__(self, name, avgAttendence: list[int], hereToday: bool):
        self.id = next(self.id_iter)
        self.name = name
        self.avgAttendence = avgAttendence
        self.hereToday = hereToday
        studentLookup[self.id] = self
    def __repr__(self) -> str:
        return self.name


class Staff:
    def __init__(self) -> None:
        self.present = 0
        self.absent = 0
        self.total = 0
    def set_section(self, grade: int, section: str):
        self.grade = grade
        self.section = section
    def calc_attendence(self, students):
        for student in students:
            if (student.hereToday):
                self.present += 1
            else:
                self.absent += 1
            self.total += 1

class User:
    def __init__(self) -> None:
        pass

    def get_attendence(self, studentId):
        print(f"{studentLookup[studentId]}'s attendence report:")
        print(f"Yearly attendence: {studentLookup[studentId].avgAttendence[0]}%")
        print(f"Monthly attendence: {studentLookup[studentId].avgAttendence[1]}%")
        print(f"Weekly attendence: {studentLookup[studentId].avgAttendence[2]}%")

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
            student.grade = grade
            student.section = section
            self.data[grade]["Sections"][section].append(student)
            self.data[grade]["No of students"] += 1
        except FullSection as a:
            print(a)
            return

    def allocate_staff(self, staff: Staff, grade: int, section: str):
        staff.set_section(grade, section)
        staff.calc_attendence(self.data[grade]["Sections"][section])
    

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
jeff = Student('Jeff', [30, 20, 50], True)
zeff = Student('Zeff', [60, 29, 90], False)
a.add_student_to_class(jeff, 2, 'b')
a.add_student_to_class(zeff, 2, 'b')
s = Staff()
a.allocate_staff(s, 2, 'b')
print(a.data)
print(s.grade)
print(s.section)
print(s.absent)
print(s.present)
print(s.total)
u = User()
u.get_attendence(5)

