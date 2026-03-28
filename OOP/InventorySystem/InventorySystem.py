class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def update_product(self, name=None, quantity=None, price=None):
        if name is not None:
            self.name = name
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        
    def __str__(self):
        return f"{self.name} | Price: {self.price} | Quantity: {self.quantity}"
    
class Inventory:
    def __init__(self):
        self.products = []
    
    def show_products(self):
        
        if self.products:
            for i, product in enumerate(self.products, start=1):
                print(f"{i}: {product}")
        else:
            print("No products available")
                
    def add_products(self, product):
        self.products.append(product)
    
    def search_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
            
        return None
    
    def remove_products(self, index):
        if 0 <= index < len(self.products):
            return self.products.pop(index)
        else:
            print("products not found.")

def init():
    print("===============================")
    print("= Inventory Management System =")
    
    inventory = Inventory()
        
    while True:
        print("===============================\n")
        print("(1) Show all product")      
        print("(2) Search New Item")
        print("(3) Add Item")
        print("(4) Update Item")
        print("(5) Remove Item")
        print("(6) Exit ")

        choice = input("Enter choice: ")        
        
        if  choice == "1":
            print("\n===== Show All Products ======")
            inventory.show_products()
                    
        elif choice == "2":
            print("\n=====  Search Products ======")
            productName = input("Product Name: ")
            product = inventory.search_product(productName)
            
            if product:
                print(product)      
            else:
                print("No products found.")
        
        elif choice == "3":
            print("\n===== Add Products ======")
            name = input("Product Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            product = Product(name, quantity, price)
            
            inventory.add_products(product)
    
        elif choice ==  "4":
            print("\n===== Update Products ======")
            
            name = input("Enter Product Name: ")
            product = inventory.search_product(name)
            
            if (product):
                print("----- leave blank if no changes -----")
                
                new_name = input("New name: ")
                new_quantity = input("New quantity: ")
                new_price = input("New price: ")
                
                product.update_product(
                    name=new_name if new_name else None,
                    quantity=new_quantity if new_quantity else None,
                    price=new_price if new_price else None
                )
                
                print("Product successfully updated.")
             
            else: 
                print("Product not found.")
                
        elif choice ==  "5":
            print("\n===== Delete Products ======")
            inventory.show_products()
            
            try: 
                index = int(input("Enter ID index to delete product: "))
                remove = inventory.remove_products(index - 1)
                
                if remove:
                    print(f"Remove: {remove}")
                    
            except ValueError:
                print("Invalid input.")
        
        elif choice == "6":
            print("Thank you for choosing our services.")
            return True
        else:
            print("Wrong input, try again.")

init() 