from admin import *
from user import *

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

    stud1.attendance = [True, True, True, False, True, True, True, True, False, True, True, True, True, False, True,
                        True, True, True, False, True, True, True, True, False, True, True, True, True, False, True]
    stud2.attendance = [True, False, False, False, True, True, True, True, False, True, True, True, True, False, True,
                        True, True, True, False, True, True, True, True, False, True, True, True, False, False, False]
    stud3.attendance = [True, True, True, False, True, True, True, True, False, True, True, True, True, False, True,
                        True, True, True, False, True, False, False, True, False, True, True, True, True, False, True]
    stud4.attendance = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                        True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

    admin.add_student_to_class(stud1, 1)
    admin.add_student_to_class(stud2, 1)
    admin.add_student_to_class(stud3, 1)
    admin.add_student_to_class(stud4, 2)

    staff1 = Staff("John", "ICT")
    staff2 = Staff("Lana", "English")

    admin.allocate_staff_to_section(staff1, 1, 1)
    admin.allocate_staff_to_section(staff2, 1, 2)


def admin_menu(admin):
    admin_choice = None
    while admin_choice != 7:

        choices = """
        1. Add Grade (Class)
        2. Add Section under Grade
        3. Add Student to Grade & Section
        4. Allocate Staff to Grade's Section
        5. Take Student Attendance
        6. Print Student Attendance
        7. Print Grades & Sections
        8. Exit
        """

        admin_choice = int(input(textwrap.dedent(choices)))

        # add grade
        if admin_choice == 1:
            admin.add_grade()
        # add section under grade
        elif admin_choice == 2:
            try:
                grade = int(input("Grade to add the section under: "))
                admin.add_section(grade)
            except ValueError:
                print("Invalid input for one of the fields")
        # add student to grade
        elif admin_choice == 3:
            try:
                print("Please enter student details")
                name = input("Student name: ")
                age = int(input("Student age: "))
                grade = int(input("Grade: "))
                student = Student(name, age)
                admin.add_student_to_class(student, grade)
            except ValueError:
                print("Invalid input for one of the fields")
        # allocate staff to grade section
        elif admin_choice == 4:
            try:
                print("Please enter Staff details")
                name = input("Staff name: ")
                department = input("Staff department: ")
                staff = Staff(name, department)
                grade_id = int(input("Grade: "))
                section_id = int(input("Section: "))
                admin.allocate_staff_to_section(staff, grade_id, section_id)
            except ValueError:
                print("Invalid input for one of the fields")
        # take student attendance for today
        elif admin_choice == 5:
            try:
                staff_id = int(input("Enter your Staff ID: "))
                staff_section = admin.find_staff_section(staff_id)
                admin.display_staffs_section(staff_id)

                absent_ids = list(input("Enter the ids of the absent students\nEnter 0 if none are absent: "))
                absent_ids = [i for i in absent_ids if i != ' ']

                if "0" not in absent_ids:
                    for absent_id in absent_ids:
                        mark_student_absent(int(absent_id), staff_section)
                mark_students_present(absent_ids, staff_section)
            except ValueError:
                print("Invalid input for one of the fields")
            except PersonNotFound as e:
                print(e)
        # print attendance for today
        elif admin_choice == 6:
            try:
                staff_id = int(input("Enter your Staff ID: "))
                staff_section = admin.find_staff_section(staff_id)
                try:
                    display_last_student_attendance(staff_section)
                except AttributeError:
                    print(f"Staff ID {staff_id} not found")
            except ValueError:
                print("Invalid input for one of the fields")
        elif admin_choice == 7:
            admin.display()
        elif admin_choice == 8:
            print("Exiting admin menu...")
        else:
            print("Invalid choice, try again: ")


def user_menu(admin):
    user_choice = None
    while user_choice != 4:

        choices = """
                1. Show Last Week's Attendance
                2. Show Last Month's Attendance
                3. Show Last Year's Attendance
                4. Exit
                """
        user_choice = int(input(textwrap.dedent(choices)))
        if user_choice == 1:
            try:
                stud_id = int(input("Enter student id: "))
                student = admin.find_student(stud_id)
                show_weekly_attendance(student)
            except ValueError:
                print("Invalid input for one of the fields")
            except PersonNotFound as e:
                print(e)
        elif user_choice == 2:
            try:
                stud_id = int(input("Enter student id: "))
                student = admin.find_student(stud_id)
                show_monthly_attendance(student)
            except ValueError:
                print("Invalid input for one of the fields")
            except PersonNotFound as e:
                print(e)
        elif user_choice == 3:
            try:
                stud_id = int(input("Enter student id: "))
                student = admin.find_student(stud_id)
                show_yearly_attendance(student)
            except ValueError:
                print("Invalid input for one of the fields")
            except PersonNotFound as e:
                print(e)
        else:
            print("Invalid choice, try again")


if __name__ == '__main__':

    admin = Admin()
    initialise(admin)
    user_admin_choice = None

    while user_admin_choice != EXIT_1:
        user_admin_choice = int(input("1. Admin \t 2. User \t 3. Exit\n"))
        if user_admin_choice == 1:
            admin_menu(admin)
        elif user_admin_choice == 2:
            user_menu(admin)
        elif user_admin_choice == 3:
            print("Exiting program")
        else:
            print("Invalid choice, try again")
