questions = ("What are potatoes? ",
             "What is my favourite attunement? ",
             "Who is maestro? ",
             "Which character uses two elements? ",
             "What is the first region in genshin? ")

options = (("A. Fruit","B. Vegetable","C. Plant","D. Life"),
           ("A. Frostdraw","B. Shadowcast","C. Flamecharm","D. Thundercall"),
           ("A. a bum","B. the goat","C. singer","D. him"),
           ("A. klee","B. durin","C. varka","D. nicole"),
           ("A. liyue","B. snezhnaya","C. mondstadt","D. inazuma"))

answers = ("B", "A", "D", "C", "C")

guesses = []

score = 0

question_num = 0

while True:

    print ("---------------------")
    print ("       DA QUIZ       ")
    print ("---------------------")

    for question_num, question in enumerate(questions):
        print("-------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A), (B), (C), (D) ").upper()
        while guess != "A" and guess != "B" and guess != "C" and guess != "D":
            print("Please enter a value from the list.")
            guess = input("Enter (A), (B), (C), (D) ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            print("Correct :D")#
            score += 1
        else:
            print("Incorrect :(")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    score = int(score / len(questions) * 100)

    print("Your score is " f"{score}%!")

    retry = input("Do you want to retry? Y/N ").upper()
    if retry == "N":
        break