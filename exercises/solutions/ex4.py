from student_generator import get_students, years

def alphabetical_names(students):
    names = []
    for student in students:
        names.append(student["name"])
    names.sort()
    return names

def students_by_year(students, year):
    by_year = []
    for student in students:
        if student["year"] is year:
            by_year.append(student)
    return by_year

def count_by_year(students):
    by_year = {}
    for year in years:
        by_year[year] = len(students_by_year(students, year))
    return by_year

def calc_student_average(student):
    grades = []
    for c in student["classes"]:
        grades.append(c["grade"])
    total = 0.0
    count = 0.0
    for grade in grades:
        total += grade
        count += 1
    return total / count

def average_by_student(students):
    averages = {}
    for student in students:
        averages[student["name"]] = calc_student_average(student)
    return averages

students = get_students()

print str.join(",", alphabetical_names(students))
print count_by_year(students)
print average_by_student(students)