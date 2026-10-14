study_hours = [2, 3, 1, 2, 0, 4, 2]

for day, hours in enumerate(study_hours, start=1):
    if hours < 2:
        print(f"Day {day}: {hours} hours")