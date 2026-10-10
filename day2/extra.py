name= "aziz"
Age = 25
daily_Study_hours = 2
print(name)
print(Age)
print('daily daily_Study_hours')
print("weekly study hours",daily_Study_hours*7)



def person_hours(hours):
    if hours >=2:
        return "Ready for that"
    else:
        return "not ready"
    
    
    
for i in range(1,4):
    check = person_hours(i)
    print(f"{i} hours:{check}")
    
    


for numbers in range(1,11):
    if numbers % 2 == 0:
        print(numbers)
        
        
        
        
def calculate_total(price, quantity):
    total_cost = price * quantity
    return total_cost

Cost1 = calculate_total(25,4)
Cost2 = calculate_total(10,3)
Cost3= calculate_total(99.99,2)
print(Cost1)
print(Cost2)
print(Cost3)



Programming = ["ml","ai","ds","st","bs"]
print(Programming[0])
print(Programming[-1])

for Programming in Programming:
    print(Programming)





Student = {
    "name" :"Aziz",
    "target_role" : "AI enginner",
    "daily_hours" : 2,
    "days_completed" : 1
}
print(Student["name"])
print(Student["target_role"])
print(Student["daily_hours"])
Student["days_completed"]  = 2
print(Student["days_completed"])




def final_check(hours):
    if hours < 2:
        return "keep practicing"
    elif hours == 2:
        return "GOal Achived"
    else:    
        return "Excllent"
    
for i in range(1,5):
    must_check = final_check(i)
    print(f"{i} hours:{must_check}")