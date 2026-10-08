import random


def run_quiz():
    questions = [
        {
            "question": "What keyword is used to define a function in python?",
            "options": ["a)func", "b)def", "c)function", "d)define"],
            "answer": "b"
        },
        {
            "question": "Which data type is immutable?",
            "options": ["a)list", "b)dictionary", "c)tuple", "d)set"],
            "answer": "c"
        },
        {
            "question": "How do you insert comments in Python code?",
            "options": ["a)//", "b)<!-- -->", "c)/* */", "d)#"],
            "answer": "d"
        },
        {
            "question": "Which method adds an item to the end of a list?",
            "options": ["a)append()", "b)add()", "c)insert()", "d)push()"],
            "answer": "a"
        },
        {
            "question": "What is the result of 10//3 in Python?",
            "options": ["a)3.33", "b)3", "c)1", "d)3.0"],
            "answer": "b"
        }
    ]

    shuffle_option = input("Do you want to shuffle questions?(y/n): ").strip().lower()
    if shuffle_option == 'y':
        random.shuffle(questions)

    score = 0
    print("\n---Starting Quiz ---")

    for idx, q in enumerate(questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        for opt in q['options']:
            print(opt)

        user_ans = input("Your answer (a/b/c/d): ").strip().lower()
        if user_ans == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer was '{q['answer']}'.")

    print(f"\nQuiz Finished! Final Score: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()
