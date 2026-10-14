study_hours=[1,4,7,9,2,1,1,7,5,4,6,3]
count = 0
for day, hours in enumerate(study_hours , start=1):
    if hours <2:
        count = count+1
        
print(count)