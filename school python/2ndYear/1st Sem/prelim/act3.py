h = int(input("What is your height? "))
w = float(input("What is your weight? "))

h /= 100
bmi = w / (h * h)

print(f"The BMI is {bmi}")