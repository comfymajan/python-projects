from question import question
questions = [
    question(
        "Whats the capital of Spain?",
        ["A.London","B.Paris","C.Berlin","D.Madrid"],
        "D"
    ),
    question(
        "What is the capital of USA?",
    ["A.NewYork","B.Washington,D.C","C.SanDiego","D.LasVegas"],
        "B"
    ),
    question(
        "What is the capital of UK?",
        ["A.London","B.Rome","C.Manchester","D.Kabol"],
        "A"
    ),
    question(
        "What is the capital of Iran?",
        ["A.IslamAbad","Kabol","Tehran","Mashhad"],
        "C"
    )
]
def run_test(questions):
    score = 0
    for question in questions:
        print("\n--------------------")
        question.show_question()
        answer = input("Your answer: ")
        while answer not in ["A","B","C","D"]:
            print("Invalid answer")
            answer = input("Your answer: ")
        if answer == question.answer:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
            print("Correct answer:" + question.answer)
    print("\n--------------------")
    print(" Your score:" + str(score) + "/" + str(len(questions)))
    percentage = score / len(questions)*100
    print("Your percentage:" + str(percentage) + "%")
    if percentage ==100:
        print("Congratulations!")
    elif percentage >= 75:
        print("Very Good!")
    elif percentage >= 50:
        print("Good!")
    else:
        print("Failed!")
        print("Keep practicing!")
while True:
    run_test(questions)
    again = input("\nDo you want to play again? (y/n)?")
    if again != "y":
        print("Thanks for playing!")
        break