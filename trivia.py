import requests
import json

repeat = True
marks = 0

print("Welcome to trivia game")

while repeat == True:
    trivia = requests.get("https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=boolean")

    trivia_dict = json.loads(trivia.text)

    que = trivia_dict["results"][0]["question"]
    ans = trivia_dict["results"][0]["correct_answer"]

    print("Your question is: ", que)
    user_ans = input("Enter your answer True/False: ")
    if user_ans.lower() == ans.lower():
        print("Your answer is currect!")
        marks += 1
    else:
        print("Wrong answer.")
    play_again = input("Do you want to try another one? (type quit to end the trivia)")
    if play_again.lower() == "quit":
        repeat = False

print("Thanks for playing. your total score is ", marks)