from random import randint

names = ["john", "amy", "kyle", "lauren", "ricky", "barbara", "sadie", "beau", "savannah"]
years = ["freshman", "sophomore", "junior", "senior"]
classes = ["math", "english", "science", "art"]

def get_students():
    students = []
    for name in names:
        student = {
            "name": name,
            "year": years[randint(0,len(years) - 1)],
            "classes": []
        }
        for class_name in classes:
            student["classes"].append({
                "class": class_name,
                "grade": randint(60, 100)    
            })
        students.append(student)
    return students