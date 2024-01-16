import time
import random

questions = [{"What is in east of Pakistan": ("China", "France", "India", "Afghanistan")},
             {"What is in west of Pakistan": ("China", "France", "India", "Afghanistan")},
             {"What is in north of Pakistan": ("China", "France", "India", "Afghanistan")},
             {"What is in east of Pakistan": ("China", "France", "India", "Afghanistan")},
             ]
dic = {"What is in east of Pakistan": ("China", "France", "India", "Afghanistan")}

def chr(string):
    for char in string + "\n":
        # time.sleep(0.05)
        print(char, end="")
        # time.sleep(0.08)





i = 0
# print(questions[0].keys())
# print(random.choice(questions[0]))
while True:
    quest = random.choice(questions)
    time.sleep(0.5)
    chr("The game starts in few seconds...")
    time.sleep(0.2)
    chr("Get ready...")
    time.sleep(0.1)
    chr("Here, is your first question!")
    # print(f"Q:{quest[0]}\n1.{}")
    if quest in questions:
        questions.remove(quest)
    print(questions)
    break
