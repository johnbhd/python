age = int(input("Enter your age: "))


regmovie = 0
movie3d = 0
imaxmovie = 0
tp = 0
text1 = "Enter the type of movie: " 
text2 = "Choose only 1-3 option"

print("[1] Regular\n[2] 3D\n[3] IMAX")

if age >= 0 and age <= 12:
   
    response = int(input(f"{text1}"))

    if response == 1:
        regmovie = 150
        tp = regmovie

    elif response == 2:
        movie3d = 250
        tp = movie3d

    elif response == 3:
        imaxmovie = 350
        tp = imaxmovie
    else: 
        print(text2)
elif age >= 13 and age <= 59:
    response = int(input(f"{text1}"))

    if response == 1:
        regmovie = 300
        tp = regmovie

    elif response == 2:
        movie3d = 450
        tp = movie3d

    elif response == 3:
        imaxmovie = 600
        tp = imaxmovie
    else: 
        print(text2)

elif age >= 60:
    response = int(input(f"{text1}"))

    if response == 1:
        regmovie = 100
        tp = regmovie

    elif response == 2:
        movie3d = 150
        tp = movie3d

    elif response == 3:
        imaxmovie = 200
        tp = imaxmovie
    else: 
        print(text2)

else:
    print("Invalid Age")

print(f"Ticket Price: {tp} pesos")