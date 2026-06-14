question1 = {"question": "What are potatoes?","options":["A. Fruit","B. Vegetable","C. Plant", "D. Life"], "answer": "B" }

question2 = {"question": "What is my favourite attunement?","options":["A. Frostdraw","B. Shadowcast","C. Flamecharm", "D. Thundercall"], "answer": "A" }

question3 = {"question": "Who is maestro?","options":["A. a bum","B. the goat","C. singer", "D. him"], "answer": "D" }

question4 = {"question": "Which character uses two elements?","options":["A. klee","B. durin","C. varka", "D. nicole"], "answer": "C" }

question5 = {"question": "What is the first region in genshin?","options":["A. liyue","B. snezhnaya","C. mondstadt", "D. inazuma"], "answer": "C" }

quiz = [question1, question2, question3, question4, question5]

guesses = []

score = 0

question_num = 0

while True:

    print ("---------------------")
    print ("       DA QUIZ       ")
    print ("---------------------")

    for q in quiz:
        print("-------------------")
        print(q["question"])
        for opt in q["options"]:
            print(opt)

        guess = input("Enter (A), (B), (C), (D) ").upper()
        while guess != "A" and guess != "B" and guess != "C" and guess != "D":
            print("Please enter a value from the list.")
            guess = input("Enter (A), (B), (C), (D) ").upper()
        guesses.append(guess)
        if guess == q["answer"]:
            print("Correct :D")#
            score += 1
        else:
            print("Incorrect :(")
            print(f"{q["answer"]} is the correct answer")
        question_num += 1

    score = int(score / len(quiz) * 100)

    print("Your score is " f"{score}%!")

    retry = input("Do you want to retry? Y/N ").upper()
    if retry == "N":
        break