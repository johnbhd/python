while True:
    birth = int(input("Enter your birth month number: "))

    if birth >= 1 and birth <= 12:
        if birth == 1:
            month = "January"
        elif birth == 2:
            month = "February"
        elif birth == 3:
            month = "March"
        elif birth == 4:
            month = "April"
        elif birth == 5:
            month = "May"
        elif birth == 6:
            month = "June"
        elif birth == 7:
            month = "July"
        elif birth == 8:
            month = "August"
        elif birth == 9:
            month = "September"
        elif birth == 10:
            month = "October"
        elif birth == 11:
            month = "November"
        elif birth == 12:
            month = "December"

        print(f"You birth is {month}.")
        break
    else:
        print("Invalid input!")