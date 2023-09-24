from Question import Question
import time

question_prompts = [
    "1. In Vinland Saga, where did Leif Ericon sell the\n\
    narwhal horns that was acquired from Halfdan?\na.) Greece\nb.) Rome\nc.) Greenland\n\n",
    "2. In Monogatari, how many pages of the light novel\n\
    were dedicated to the infamous toothbrush scene?\na.) 10\nb.) 7.5\nc.) 3.5\n\n",
    "3. In Attack on Titan, who turned into a bird?\na.) Reiner\nb.) Eren\nc.) Sasha\n\n",
    "4. How many Dragon Balls are there?\na.) 7\nb.) 8\nc.) 9\n\n",
    "5. What is the jersey number of Kobayakawa Sena in Eyeshield 21?\na.) 69\nb.) 21\nc.) 17\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You scored " + str(score) + "/5")


run_test(questions)
time.sleep(5)