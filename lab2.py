name = input("Enter your name here: ")
selectnumber = int(input(f"Hi {name}! Pick a number between 1 and 100: "))
print(f"You picked {selectnumber}.")

if (selectnumber % 2 != 0) and 0 < selectnumber < 60 :
    print(f"{selectnumber}. Odd and less than 60.")
    option = input("Would you like to select another number? Type Y or N. ")
elif (selectnumber % 2 == 0) and 2 <= selectnumber <= 24:
    print(f"{selectnumber}. Even and less than 25.")
    option = input("Would you like to select another number? Type Y or N. ")
elif (selectnumber % 2 == 0) and 26 <= selectnumber <= 60:
    print(f"{selectnumber}. Even and between 26 and 60 inclusive.")
    option = input("Would you like to select another number? Type Y or N. ")
elif (selectnumber % 2 == 0) and 60 < selectnumber:
    print(f"{selectnumber}. Even and greater than 60.")
    option = input("Would you like to select another number? Type Y or N. ")
elif (selectnumber % 2 != 0) and 60 < selectnumber:
    print(f"{selectnumber}. Odd and greater than 60.")
    option = input("Would you like to select another number? Type Y or N. ")
elif selectnumber < 0:
    print("Error. Please select a positive integer between 1 and 100.")

while option == "Y":
    selectnumber = int(input(f"Hi again, {name}! Pick a number between 1 and 100: "))

    if (selectnumber % 2 != 0) and 0 < selectnumber < 60 :
        print(f"{selectnumber}. Odd and less than 60.")
        option = input("Would you like to select another number? Type Y or N. ")
    elif (selectnumber % 2 == 0) and 2 <= selectnumber <= 24:
        print(f"{selectnumber}. Even and less than 25.")
        option = input("Would you like to select another number? Type Y or N. ")
    elif (selectnumber % 2 == 0) and 26 <= selectnumber <= 60:
        print(f"{selectnumber}. Even and between 26 and 60 inclusive.")
        option = input("Would you like to select another number? Type Y or N. ")
    elif (selectnumber % 2 == 0) and 60 < selectnumber:
        print(f"{selectnumber}. Even and greater than 60.")
        option = input("Would you like to select another number? Type Y or N. ")
    elif (selectnumber % 2 != 0) and 60 < selectnumber:
        print(f"{selectnumber}. Odd and greater than 60.")
        option = input("Would you like to select another number? Type Y or N. ")
    elif selectnumber < 0:
        print("Error. Please select a positive integer between 1 and 100.")

else:
    print(f"Thanks for participating, {name}! See you later!")