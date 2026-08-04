import random

pc_guess=random.randint(1,10)

while True:
    user_guess=int(input("Enter number bw 1 and 10 : "))
    if user_guess>10:
            print("Please select a number bw 1 and 10")
    elif pc_guess==user_guess:
        print("You Guessed Correctly")
        break
    else:
        print("You Guessed Incorrectly")
