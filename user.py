import math

YEAR = 190
MONTH = 20
WEEK = 5


def show_weekly_attendance(student):
    if len(student.attendance) >= WEEK:
        last_week = student.attendance[-WEEK:-1]
        count = 0
        for day in last_week:
            if day:
                count += 1

        print(f"Student {student.id} named {student.name}")
        print(f"Attended {count}/{WEEK} classes last week")
        print(f"That is {math.trunc((count / WEEK) * 100)}% attendance last week")
    else:
        print("This student has not yet attended a full week of classes")
        count = 0
        for day in student.attendance:
            if day:
                count += 1
        print(f"They have attended {count} out of {len(student.attendance)} classes")
        print(f"That is {math.trunc((count/len(student.attendance) * 100))}% attendance")


def show_monthly_attendance(student):
    if len(student.attendance) >= MONTH:
        last_month = student.attendance[-MONTH:-1]
        count = 0
        for day in last_month:
            if day:
                count += 1

        print(f"Student {student.id} named {student.name}")
        print(f"Attended {count}/{MONTH} classes last month")
        print(f"That is {math.trunc((count/MONTH) * 100)}% attendance last month")
    else:
        print("This student has not yet attended a full month of classes")
        count = 0
        for day in student.attendance:
            if day:
                count += 1
        print(f"They have attended {count} out of {len(student.attendance)} classes")
        print(f"That is {math.trunc((count/len(student.attendance) * 100))}% attendance")


def show_yearly_attendance(student):
    if len(student.attendance) >= YEAR:
        last_year = student.attendance[-YEAR:-1]
        count = 0
        for day in last_year:
            if day:
                count += 1

        print(f"Student {student.id} named {student.name}")
        print(f"Attended {count}/{YEAR} classes last year")
        print(f"That is {math.trunc((count / YEAR) * 100)}% attendance last year")
    else:
        print("This student has not yet attended a full year of classes")
        count = 0
        for day in student.attendance:
            if day:
                count += 1
        print(f"They have attended {count} out of {len(student.attendance)} classes")
        print(f"That is {math.trunc((count/len(student.attendance) * 100))}% attendance")
