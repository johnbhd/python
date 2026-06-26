n = int(input("Enter Initial Number: "))
i = int(input("Enter No. of Iterations: "))
diff = int(input("Enter Common Difference: "))
sum = 0
prod = 1
sum_str = ""
prod_str = ""

for num in range(i):
    term = n + (num * diff)
    sum += term
    prod *= term
    
    if num == 0:
        sum_str = str(term)
        prod_str = str(term)
    else: 
        sum_str += " + " + str(term)
        prod_str += " * " + str(term)

print(f"Sum: {sum_str} = {sum:,}")
print(f"Product: {prod_str} = {prod:,}")