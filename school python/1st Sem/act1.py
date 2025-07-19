numMeal = int(input("How many times a week do you eat at the student cafeteria? "))
pLunch = float(input("The price of a typical student lunch? "))
moneySpend = float(input("How much money do you spend on groceries in a week? "))

weekly = (numMeal * pLunch) + moneySpend
daily = weekly / 7

print("\nAverage food expenditure: ")
print(f"Daily: {daily} pesos")
print(f"Weekly: {weekly} pesos")