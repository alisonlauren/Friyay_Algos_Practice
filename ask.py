user_input = int(input("Hey user! Can you guess the secret number? "))
def number(number, choice):
    if choice != number:
        print("wrong")
        choice = int(input("try again?"))
    else:
        print("winner")


number(7, user_input)

def findSecretNum(choice, number):
    while number != choice:
        if choice > number:
            print("aw sorry, you guessed too high")
            choice = int(input("Try again? "))
        elif choice < number:
            print("no way- your number is too small")
            choice = int(input("Try again? "))
        else:
            print("You guessed it!")

findSecretNum(user_input, 33)