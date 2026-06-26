sideA = int(input("Enter the length of side A: "))
sideB = int(input("Enter the length of side B: "))
sideC = int(input("Enter the length of side C: "))

if sideA == sideB == sideC:
    print("Equilateral Triangle")
elif (sideA == sideB) or (sideA == sideC) or (sideC == sideB):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")