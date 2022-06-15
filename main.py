from nick_admin import *

import textwrap

ADMIN = 1
USER = 2
EXIT_1 = 3
EXIT_ADMIN = 10
EXIT_USER = 10


def initialise(admin):
    admin.add_grade()
    admin.add_grade()

    admin.add_section(1)
    admin.add_section(1)
    admin.add_section(1)
    admin.add_section(2)

    stud1 = Student("Nicolas", 15)
    stud2 = Student("Caoimhe", 16)
    stud3 = Student("Morgan", 14)
    stud4 = Student("Bill", 17)

    admin.add_student_to_class(stud1, 1)
    admin.add_student_to_class(stud2, 1)
    admin.add_student_to_class(stud3, 1)
    admin.add_student_to_class(stud4, 2)

    staff1 = Staff("John", "ICT")
    staff2 = Staff("Lana", "English")

    admin.allocate_staff_to_section(staff1, 1, 1)
    admin.allocate_staff_to_section(staff1, 1, 2)


def admin_menu(admin):
    choices = """
    1. Add Grade (Class)
    2. Add Section under Grade
    3. Add Student to Grade & Section
    4. Allocate Staff to Grade's Section
    5. Take Student Attendance
    6. Print Student Attendance
    """

    admin.display()
    admin_choice = int(input(textwrap.dedent(choices)))

    # add grade
    if admin_choice == 1:
        admin.add_grade()
    # add section under grade
    elif admin_choice == 2:
        grade = int(input("Grade to add the section under: "))
        admin.add_section(grade)
    # add student to grade
    elif admin_choice == 3:
        print("Please enter student details")
        name = input("Student name: ")
        age = int(input("Student age: "))
        grade = int(input("Grade: "))
        student = Student(name, age)
        admin.add_student_to_class(student, grade)
    # allocate staff to grade section
    elif admin_choice == 4:
        print("Please enter Staff details")
        name = input("Student name: ")
        department = input("Staff department: ")
        staff = Staff(name, department)
        grade_id = int(input("Grade: "))
        section_id = int(input("Section: "))
        admin.allocate_staff_to_section(staff, grade_id, section_id)
    # take student attendance for today
    elif admin_choice == 5:
        # enter staff id
        staff_id = int(input("Enter your Staff ID: "))
        # print all students for the Grade Section
        section_iterator = filter(lambda s: s.staff.id == staff_id, admin.grades.sections)
        grade_list = list(section_iterator)
        grade_list[0].displayStudents()

        # ask which ones are absent, enter 0 for no absences
        # for all absent ids
        # mark student as absent
        # for all non-absent ids
        # mark them as present
        pass
    # print attendance for today
    elif admin_choice == 6:
        admin.display_last_student_attendance()
        pass
    else:
        print("Invalid choice, try again: ")


def user_menu():
    pass


if __name__ == '__main__':

    admin = Admin()
    initialise(admin)
    user_admin_choice = int(input("1. Admin \t 2. User \t 3. Exit\n"))

    while user_admin_choice != EXIT_1:
        if user_admin_choice == 1:
            admin_menu(admin)
        elif user_admin_choice == 2:
            user_menu()
        elif user_admin_choice == 3:
            print("Exiting program")
        else:
            print("Invalid choice, try again")
