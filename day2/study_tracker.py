name = input("Enter your name: ")
hours = int(input("How many hours you study today? "))

def Study_hours(hours):
    if hours>=2:
        return "Chass a gye"
    else:
       return "haly hor Kaam kr puttra"
    
    
weekly_hours = hours* 7
print(weekly_hours)
print("\n----Study REport-----")
print("Name:",name)
print("How many hours",hours)
print("Progress",Study_hours(hours))

