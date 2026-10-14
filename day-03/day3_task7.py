study_hours = [1, 4, 7, 9, 2, 1, 1, 7, 5, 4, 6, 3]

for day,hour in enumerate(study_hours,start=1):
    if hour >= 4:
        print(f"day {day} : {hour} in hours")