from question_class import Question

question_prompts = [
    "What colours are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colours are Bananas?\n(a) Blue\n(b) Red\n(c) Yellow\n\n",
    "What colours are Strawberries?\n(a) Magenta\n(b) Blue\n(c) Red\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")


run_test(questions)


