questions = {
    "Which keyword is used to define a function in Python?": "def",
    "Which function is used to display output in Python?": "print",
    "Which symbol is used for comments in Python?": "#",
    "Which data type is used to store True or False?": "bool",
    "Which function is used to get input from the user?": "input"
}
score = 0
print("Python Quiz")
for question, answer in questions.items():
    user_answer = input(question + " ").lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", answer)
print("Your score:", score, "/",len(questions))
