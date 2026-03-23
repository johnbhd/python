#Check even num user input - 8/23/25  4:52pm

def Main():
    while True:        
        num = input("Enter a number: ")
        if not num.isdigit():
            print("Input number only.\n")
            continue
        num = int(num)
        
        ch = ["even", "odd"]
        
        if (num % 2 == 0):
            print(ch[0])
        else:
            print(ch[1])
            
        print("")
        
Main()    