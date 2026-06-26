allitem = "\nItems: \n"

for i in range(1, 4):
  item = input(f"Item{i}: ")
  price = int(input(f"Item{i} price: "))
  allitem = allitem + f"\tItem{i}: {item} - {price} pesos \n"
  
print(allitem)