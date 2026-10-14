study_hours = [1, 4, 7, 9, 2, 1, 1, 7, 5, 4, 6, 3]

total = 0
for hour in study_hours:
    total = hour +total
    
total_days = len(study_hours)

avrage_days =total /total_days
print("avrage days" , round(avrage_days,2))
