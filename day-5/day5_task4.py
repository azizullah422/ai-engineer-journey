skills = ["Python", "Git", "Python", "SQL", "FastAPI", "Git"]

unique_Skills = set(skills)
print(unique_Skills)
print(len(unique_Skills))
if "Python" in unique_Skills:
    print("Match FOund")
else:
    print("match not found")