import random

##1. Question One: With the given list below, loop through each name and make them say hello in the terminal.
name_list = ['Rachel', 'Ross', 'Chandler', 'Monica']

def sayHello(list): 
    for name in list:
        print(f" Hi, I'm {name}")
sayHello(name_list)

#or
# for name in name_list:
#     print(f" Hi, I'm {name}")
## Your output should look like "Hi, I'm __insert name____ " for each name.


##2. Question Two: With the given list below, create a function that adds one charachter.
name_list2 = ['Rachel', 'Ross', 'Chandler', 'Monica']

def add_character(list, name):
    list.append(name)
    print(list)
name_list2 = add_character(name_list2, 'ted')

##or
# name_list2.append('ted mosby')
# print(name_list2)
# name_list2.remove(name_list2[0])
# print(name_list2)

##3. Question Three: Create a function that has secret number and asks the user what it is.
## If the user gets the answer wrong, have it print "wrong number", until they guess correctly.

user_input = int(input("Hey user! Can you guess the secret number? "))

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


# user_input = int(input("Hey user! Can you guess the secret number? "))

# while 33 != user_input:
#     if user_input > 33:
#         print("aw sorry, you guessed too high")
#         user_input = int(input("Try again? "))
#     elif user_input < 33:
#         print("no way- your number is too small")
#         user_input = int(input("Try again? "))
#     else:
#         print("You guessed it!")

##4. Question 4: Create a Magic Eight Ball. Have the user ask a question, and then create a function that
## will randomly generate "yes", "no", "maybe one day", etc.

user_input1 = input("Ask magic eight ball a question: ")
magic8_answers = ["yes", "no", "not in a million years", "keep dreaming", "oh for sure, you got it", "Knowing you, I wouldn't"]
# print(random.choice(magi))

def askMagic(input, list):
    while True:
        print(random.choice(list))
        break

askMagic(user_input, magic8_answers)






    







