import itertools


class InvalidSectionId(Exception):
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
        # fill current section up, before creating a new one
        if len(self.sections[-1].students) < self.max_students_per_section:
            self.sections[-1].add_student(student)
        else:
            new_section = GradeSection()
            new_section.add_student(student)
            self.sections.append(new_section)

    def display(self):
        print(self.id, end="\t")
        print(self.max_students_per_section, end="\t")
        print(len(self.sections), end="\t")
        for section in self.sections:
            print(f"{int_id_to_letter(section.id)},", end="")


class GradeSection:
    id_iter = itertools.count(1)

    def __init__(self, staff=None):
        self.id = next(self.id_iter)
        self.students = list()
        self.staff = staff

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print("Students:")
        for student in self.students:
            print(student.display())

    def display(self):
        print(int_id_to_letter(self.id))
        try:
            print("Teacher: ", end="")
            print(self.staff.display())
        except AttributeError:
            print("Not yet allocated")

        self.display_students()


class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}", end=" ")


class Student(Person):
    id_iter = itertools.count(1)

    def __init__(self, name, age):
        self.id = next(self.id_iter)
        super().__init__(name)
        self.age = age

    def display(self):
        print(f"ID: {self.id}", f"Name: {self.name}", f"Age: {self.age}",  end=" ")


class Staff(Person):
    id_iter = itertools.count(1)

    def __init__(self, name, department):
        self.id = next(self.id_iter)
        super().__init__(name)
        self.department = department

    def display(self):
        print(f"ID: {self.id} {self.name} from {self.department}", end=" ")


class Admin:

    def __init__(self):
        self.grades = list()

    # add classes
    def add_grade(self):
        # print("Adding grade")
        self.grades.append(Grade())

    def add_section(self, grade_id):
        # print(f"Adding section to grade {grade_id}")
        grade_iterator = filter(lambda g: g.id == grade_id, self.grades)
        grade_list = list(grade_iterator)
        section = GradeSection()
        grade_list[0].add_section(section)

    def add_student_to_class(self, student, grade_id):
        grade_iterator = filter(lambda g: g.id == grade_id, self.grades)
        grade_list = list(grade_iterator)
        grade_list[0].add_student(student)

    def allocate_staff_to_section(self, staff, grade_id, section_id):
        grade_iterator = filter(lambda g: g.id == grade_id, self.grades)
        grade_list = list(grade_iterator)
        section_iterator = filter(lambda s: s.id == section_id, grade_list[0].sections)
        section_list = list(section_iterator)
        section_list[0].staff = staff

    def print_last_student_attendance(self):
        pass

    def display(self):
        print("Grade \t Max Students in Section \t No. of Sections \t Sections")
        for grade in self.grades:
            print(grade.display())
        print("Sections: ")
        for grade in self.grades:
            for section in grade.sections:
                section.display()
    # add sections
    # add students to classes
    # allocate staff to classes
    #
