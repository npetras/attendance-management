import itertools
import os
import random


class InvalidSectionId(Exception):
    pass


class PersonNotFound(Exception):
    pass


def int_id_to_letter(int_id):
    int_to_letter = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        8: "h",
        9: "i",
        10: "k"
    }
    if 0 < int_id <= 10:
        return int_to_letter[int_id]
    else:
        raise InvalidSectionId(f"Invalid ID {int_id} was provided")


class Grade:
    id_iter = itertools.count(1)
    max_students_per_section = 20

    def __init__(self):
        self.id = next(self.id_iter)
        self.sections = list()

    def add_section(self, section):
        self.sections.append(section)

    def add_student(self, student):
        # fill current sections up, before creating a new one
        for section in self.sections:
            if len(section.students) < self.max_students_per_section:
                section.add_student(student)
                break
        else:
            new_section = GradeSection(len(self.sections) + 1)
            new_section.add_student(student)
            self.sections.append(new_section)

    def display(self):
        print(self.id, end="\t")
        print(self.max_students_per_section, end="\t")
        print(len(self.sections), end="\t")
        for section in self.sections:
            print(f"{int_id_to_letter(section.id)},", end="")


class GradeSection:

    def __init__(self, gs_id, staff=None):
        self.id = gs_id
        self.students = list()
        self.staff = staff

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print("Students:")
        for student in self.students:
            print(student.display())

    def display(self):
        print(f"Section {int_id_to_letter(self.id)}")
        try:
            print("Teacher: ", end="")
            print(self.staff.display())
        except AttributeError:
            print("Not yet allocated")

        self.display_students()


class Person:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    names = dir_path + "./names.txt"
    firstnames = []
    surnames = []
    with open(names) as n:
        for line in itertools.islice(n, 0, 60):
            firstnames.append(line[0:-1])
        for line in itertools.islice(n, 0, 60):
            surnames.append(line[0:-1])

    
    def __init__(self):
        self.name = self.firstnames[random.randint(0, 59)] + " " + self.surnames[random.randint(0, 59)]

    def display(self):
        print(f"Name: {self.name}", end=" ")


class Student(Person):
    id_iter = itertools.count(1)

    def __init__(self):
        self.id = next(self.id_iter)
        super().__init__()
        self.age = random.randint(11, 18)
        self.attendance = [bool(random.getrandbits(1)) for i in range(100)]

    def display(self):
        print(f"ID: {self.id}", f"Name: {self.name}", f"Age: {self.age}", end=" ")


class Staff(Person):
    id_iter = itertools.count(1)

    def __init__(self, name, department):
        self.id = next(self.id_iter)
        super().__init__()
        self.department = department

    def display(self):
        print(f"ID: {self.id} {self.name} from {self.department}", end=" ")


def mark_student_absent(absent_id, section):
    try:
        student_filter = filter(lambda s: s.id == absent_id, section.students)
        student_list = list(student_filter)
        student_list[0].attendance.append(False)
    except IndexError:
        print(f"Student {absent_id} not found ")


def mark_students_present(absent_ids, section):
    for student in section.students:
        if str(student.id) not in absent_ids:
            student.attendance.append(True)


def display_last_student_attendance(section):
    for student in section.students:
        present = ""
        if student.attendance[-1]:
            present = "Present"
        else:
            present = "Absent"
        print(f"{student.name} was {present}")


class Admin:

    def __init__(self):
        self.grades = list()

    # add classes
    def add_grade(self):
        self.grades.append(Grade())

    def add_section(self, grade_id):
        try:
            grade_iterator = filter(lambda g: g.id == grade_id, self.grades)
            grade_list = list(grade_iterator)
            section_id = len(grade_list[0].sections) + 1
            section = GradeSection(section_id)
            grade_list[0].add_section(section)
        except IndexError:
            print(f"The grade {grade_id} does not exist for the new section to be added")

    def add_student_to_class(self, student, grade_id):
        try:
            grade_iterator = filter(lambda g: g.id == grade_id, self.grades)
            grade_list = list(grade_iterator)
            grade_list[0].add_student(student)
        except IndexError:
            print(f"The grade {grade_id} does not exist for the new student {student.id} named {student.name}")

    def allocate_staff_to_section(self, staff, grade_id, section_id):
        section_iterator = None
        try:
            grade_iterator = filter(lambda g: g.id == grade_id, self.grades)
            grade_list = list(grade_iterator)
            section_iterator = filter(lambda s: s.id == section_id, grade_list[0].sections)
        except IndexError:
            print(f"The grade {grade_id} does not exist for the new staff member")
        try:
            section_list = list(section_iterator)
            section_list[0].staff = staff
        except TypeError:
            print(f"The grade {grade_id} does not exist for the new staff member")
        except IndexError:
            print(f"The section {section_id} does not exist for the new staff member")

    def find_staff_section(self, staff_id):
        staff_section = None
        for grade in self.grades:
            for section in grade.sections:
                try:
                    if section.staff.id == staff_id:
                        staff_section = section
                        break
                except AttributeError:
                    continue
        if staff_section is None:
            raise PersonNotFound(f"Person ID {staff_id} was not found")
        else:
            return staff_section

    def find_student(self, student_id):
        student_found = None
        for grade in self.grades:
            for section in grade.sections:
                for student in section.students:
                    try:
                        if student.id == student_id:
                            student_found = student
                            break
                    except AttributeError:
                        continue
        if student_found is None:
            raise PersonNotFound(f"Person ID {student_id} was not found")
        else:
            return student_found

    def display_staffs_section(self, staff_id):
        section = self.find_staff_section(staff_id)
        section.display_students()

    def display_grades(self):
        print("Grades", end=" ")
        for grade in self.grades:
            print(grade.id, end=" ")
        print()

    def display(self):
        print("Grade \t Max Students in Section \t No. of Sections \t Sections")
        for grade in self.grades:
            print(grade.display())
        for grade in self.grades:
            print(f"Grade {grade.id}")
            for section in grade.sections:
                section.display()
