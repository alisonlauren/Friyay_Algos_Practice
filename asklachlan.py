import random 

user_input2 = input("Ask Lachlan a question: ")
lachlan_answers = ["it depends", "well, it depends", "in that case- it depends", "hmm, depends honestly!"]
def askLachlan(input, list):
    if input == "should i make my web page chartruese":
        print("hell yes")
    elif input == "waffles" or "pancakes":
        print("Breakfast is the most important meal of the day")
    else:
        print(random.choice(list))
    

askLachlan(user_input2, lachlan_answers)