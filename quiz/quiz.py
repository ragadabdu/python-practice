# 

import random

games = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["Python", "JavaScript", "C++", "Java"],
        "answer": "JavaScript"
    },
    {
        "question": "What is 7 x 8?",
        "options": ["54", "56", "64", "58"],
        "answer": "56"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Mark Twain", "Jane Austen", "Charles Dickens"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "Mars"
    }
]

random.shuffle(games)

score = 0

for game in games:

    print(f"\n Your questions is: {game['question']}")

    for i, option in enumerate(game['options'], start =1):
        print(f"{i}. {option}")
        
    user_ans = (input("Pick your answer: ")).strip()

    if user_ans.isdigit() and int(user_ans) <= len(game["options"]):
        chosen_option = game["options"][int(user_ans) - 1]

        if chosen_option == game["answer"]:
            score += 1
    else:
        print("Invalid choice. Skipping question.")


if score > len(games):
    print(f"This is your score: {score}/{len(games)}, you won.")
else:
    print(f"This is your score: {score}/{len(games)}, you lost.")
    
