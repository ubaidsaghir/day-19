students = [
    {"name": "Ubaid", "marks": 88, "attendance": 92},
    {"name": "Ali", "marks": 72, "attendance": 95},
    {"name": "Ahmed", "marks": 91},
    {"name": "Ahsan", "marks": 89, "attendance": 94},
]


def get_top_students(student_list):
    medal_students = []
    for std in student_list:
        try:
             if std["marks"]>=85 and std["attendance"]>=90:
                 medal_students.append({"name":std["name"],"marks":std["marks"],"attendance":std["attendance"]})
        except KeyError:
            print("Attenance missing for student:",std.get("name","Unknown"))         
            
    medal_students.sort(key=lambda x: x["marks"],reverse=True)
    return medal_students

result = get_top_students(students)
print(result)        