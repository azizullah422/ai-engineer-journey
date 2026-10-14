study_recodrs = {
    "Day": 1,
    "hour": 3,
    "status": "completed",
    "topic": "Python"
}

for key,value in study_recodrs.items():
    print(key,value)
    
         
if study_recodrs["hour"] >= 2:
    print("target achivied")
else:
    print("keep working")
    
