
study_hours = [2, 3, 1, 2, 0, 4, 2]

print("Daily study hours:")

for day, hours in enumerate(study_hours, start=1):
    print(f"Day {day}: {hours} hours")

total = sum(study_hours)
average = total / len(study_hours)

print("Total study hours:", total)
print("Average daily hours:", round(average, 2))
