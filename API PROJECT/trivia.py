import json
import requests
import time


print("WELCOME TO TRIVIA ARENA! \nTest your knowledge in Geography\n")
time.sleep(1)
print("Stand a chance to win a columbus medal if you can answer all correctly\n")
time.sleep(3)
print("You have three tries to to answer ten questions. How far can you go?\n")
time.sleep(2)

difficulty = ''

while difficulty not in ['easy', 'medium']:
    difficulty = input("Please choose your difficulty: Easy(e) or Medium(m)?: ")
    if difficulty == 'e':
        difficulty = 'easy'
    elif difficulty == 'm':
        difficulty = 'medium'
    else:
        print("please input 'e' or 'm'")

api_endpoint = f"https://opentdb.com/api.php?amount=10&category=22&difficulty={difficulty}&type=boolean"
api_info = requests.get(
    api_endpoint,
    headers={'user-agent': 'user'},
    allow_redirects=False
).json()

results = api_info["results"]

numberOfTries = 0
score = 0

for i in range(len(results)):
    if numberOfTries == 3:
        print("Oops! Seems like you are out of tries. Try again?")
        print(score)
        break
    else:
        time.sleep(1)
        print(results[i]['question'])
        print()
        answer = ''
        while answer not in ['True', 'False']:
            answer = input("True(t) or False(f)? ")
            if answer == "t":
                answer = "True"
            elif answer == "f":
                answer = "False"
            else:
                print("Please give a valid input\n")
        if answer == results[i]['correct_answer']:
            score += 1
            print("correct +1!\n")
        else:
            numberOfTries += 1
            print("Not correct!\n")
if score == 10:
    print('legend! You have won!!\n')
print(f"You scored {score} points!")