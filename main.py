from admin import *

import textwrap

ADMIN = 1
USER = 2
EXIT_1 = 3
EXIT_ADMIN = 10
EXIT_USER = 10


def admin_menu(admin):
    choices = """
    1. Add Grade (Class)
    2. Add Section under Grade
    3. Add Student to Grade & Section
    4. Allocate Staff to Grade's Section
    5. Take Student Attendance
    6. Print Student Attendance
    """
    admin_choice = int(input(textwrap.dedent(choices)))
    if admin_choice == 1:
        grade = Grade()
        admin.add_grade(grade)
    elif admin_choice == 2:
        grade = int(input("Grade to add the section under: "))
        admin.add_section(grade)
    else:
        print("Invalid choice, try again: ")


def user_menu():
    pass


if __name__ == '__main__':

    admin = Admin()

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
