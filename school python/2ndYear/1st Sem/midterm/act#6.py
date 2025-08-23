age = int(input("Enter your Age: "))

if age == 1 or age == 0:
    classfi = "Infant"
elif age == 2 or age == 3:
    classfi = "Toddler"
elif age >= 4 and age <= 6:
    classfi = "Child"
elif age >= 7 and age <= 12:
    classfi = "Kid"
elif age >= 13 and age <= 19:
    classfi = "Teenager"
elif age >= 20 and age <= 59:
    classfi = "Adult"
elif age >= 60:
    classfi = "Senior Citizen"
else: 
    classfi = "wrong input"

print(f"Age Classification: {classfi}")