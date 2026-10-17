student = {
    "name": "Aziz",
    "role": "AI Engineer",
    "hours": 2
}


student["city"] = "London"
student["hours"] = 3

print(student)
print(student["name"])
print(student["role"])
print(student["hours"])
for key, value in student.items():
    print(key, ":", value)