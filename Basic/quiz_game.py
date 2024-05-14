
# This is a simple quiz game that asks the user questions and checks if the answer is correct or not.
class Questions:

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions_prompt = [
    "who is kavin ?\na)Human\nb)alien\nc)dog\n",
    "who is kavin ?\na)Human\nb)alien\nc)dog\n",
    "who is kavin ?\na)Human\nb)alien\nc)dog\n"
]

questions = [
    Questions(questions_prompt[0], "a"),
    Questions(questions_prompt[1], "a"),
    Questions(questions_prompt[2], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))


run_test(questions)