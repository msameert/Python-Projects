""" Quiz Game using dictionary and advanced loop """

print("Welcome to Quiz Game, let's test your knowledge")

questions = [
    {
      "question":"1.What is the Capital of Pakistan",
      "options":["a)Islamabad", "b)Lahore"],
      "answer":"a"
    },
    {
       "question":"2.What is the Capital of France",
       "options":["a)Paris", "b)Venice"],
       "answer":"a"
    },
    {
       "question":"3.What is the Capital of Afghanistan",
       "options":["a)Kandahar", "b)Kabul"],
       "answer":"b"
    }
]

score = 0
    
for q in questions :
    print(q["question"])
    for option in q["options"] :
        print(option)

    user_get = input("choose your answer a or b :")

    if user_get == q["answer"] :
        print("Correct answer")
        score += 1
    else :
        print("wrong answer")

print("Your total score is", score , "/", len(questions))