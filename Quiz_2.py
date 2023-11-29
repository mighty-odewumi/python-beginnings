from Question_class_2 import Question2

question_prompts = [
    "(1). What is the current president of France?\n(a) Mike Pompeo\n(b) Chris Christie\n(c) Emmanuel Macron\n(d) Sean Connery\n\n",
    "(2). What is the name of Wizkid's latest album?\n(a) StarBoy Special\n(b) Ginger\n(c) Made In Lagos\n(d) Made In Abuleegba \n\n",
    "(3). Who wrote the book 'Hamlet'?\n(a) Horace Walpole\n(b) Kim Jong Un\n(c) Williams Shakespeare\n(d) Hillary Darlington\n\n",
    "(4). Who is the father of the internet?\n(a) Nikola Tesla\n(b) Tim Berners Lee\n(c) Elon Musk \n(d) Mark Zuckerberg\n\n",
    "(5). What is the name of the late famous Chicago rapper Juice WRLD? \n (a) Jarad Anthony Higgins\n (b) Jarad Samuel Joseph\n (c) Carlson Migos Mike\n (d) Martin Luther King\n\n",
    "(6). What is the region that was tested for asymptomatic cases in China? \n (a) Xinjiang \n (b) Hunan \n (c) Beijing\n (d) Laos\n\n",
    "(7). Who wrote the book 'Think and Grow Rich'?\n (a) Andrew Carnegie \n (b) Henry Ford \n (c) Adam Sanders \n (d) Napoleon Hill \n\n",

]

questions = [
    Question2(question_prompts[0], "c"),
    Question2(question_prompts[1], "c"),
    Question2(question_prompts[2], "c"),
    Question2(question_prompts[3], "b"),
    Question2(question_prompts[4], "a"),
    Question2(question_prompts[5], "a"),
    Question2(question_prompts[6], "d")

]


def commence_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " right.")

commence_quiz(questions)


