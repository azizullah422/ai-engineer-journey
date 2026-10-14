
study_hours = [2, 3, 1, 2, 0, 4, 2]

print("Daily study hours:")

for day, hours in enumerate(study_hours, start=1):
    print(f"Day {day}: {hours} hours")

total = sum(study_hours)
average = total / len(study_hours)

print("Total study hours:", total)
print("Average daily hours:", round(average, 2))

if total >= 14:
    print("Target achivied")
else:
    print("keep practicing")
    
    
print(max(study_hours))
print(study_hours[5])

most_hours = max(study_hours)
best_day = study_hours.index(most_hours) + 1
print(f"Most study hours: Day {best_day} — {most_hours} hours")

study_hours = [3, 5, 2, 5]

for day, hours in enumerate(study_hours, start=1):
    if hours == 5:
        print(day)
