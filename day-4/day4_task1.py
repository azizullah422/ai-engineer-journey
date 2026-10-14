student = {
    "name": "Aziz",
    "age": 25
}

study_recodrs = {
    "Day": 1,
    "hour": 2,
    "status": "commpleted"
}

print(study_recodrs["hour"])
print(study_recodrs["status"])

study_recodrs["hour"] = 3
study_recodrs["topic"] = "python"
del study_recodrs["topic"]
print(study_recodrs)

if "topic" in study_recodrs:
    print("match found")
else:
    print("topic not found")
    
print(len(study_recodrs))

for value in study_recodrs.items():
    print(value)

for value in study_recodrs.values():
    print(value)
    
    
if study_recodrs["hour"] >2:
    print("target achivied")
else:
    print("keep working")