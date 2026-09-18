questions = [
    {
        "question": "Which language are we using in this project?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for a comment in Python?",
        "options": ["A. //", "B. #", "C. <!--", "D. **"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. List"],
        "answer": "C"
    },
    {
        "question": "Which function displays text on the screen?",
        "options": ["A. input()", "B. print()", "C. display()", "D. show()"],
        "answer": "B"
    }
]


def run_quiz():
    score = 0

    print("===== STUDENT PYTHON QUIZ =====")
    print("Answer each question using A, B, C, or D.\n")

    for number, question in enumerate(questions, start=1):
        print(f"Question {number}: {question['question']}")

        for option in question["options"]:
            print(option)

        answer = input("Your answer: ").upper()

        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(
                f"Wrong! The correct answer is "
                f"{question['answer']}.\n"
            )

    percentage = (score / len(questions)) * 100

    print("===== QUIZ RESULT =====")
    print(f"Score: {score}/{len(questions)}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 60:
        print("Good performance!")
    elif percentage >= 40:
        print("Keep practicing!")
    else:
        print("Keep learning and try again!")


run_quiz()