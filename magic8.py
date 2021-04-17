import random

user_input1 = input("Ask magic eight ball a question: ")
magic8_answers = ["yes", "no", "not in a million years", "keep dreaming", "oh for sure, you got it", "Knowing you, I don't think so", "YES! Of course", "uh no dude", 'i mean maybe?']
# print(random.choice(magi))

def askMagic(input, list):
    while True:
        print(random.choice(list))
        break

askMagic(user_input1, magic8_answers)