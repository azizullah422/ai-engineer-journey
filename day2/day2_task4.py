
def check_study_hours(hours):
    if hours >= 2:
       return "Target Achieved"
    else:
        return "Keep practicing"
    return hours

for i in range(1,5):
    check = check_study_hours(i)
    print(f"{i} hours: {check}")

        