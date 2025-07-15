questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. London", "B. Berlin", "C. Paris"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "choices": ["A. Central Processing Unit", "B. Computer Power Unit", "C. Core Processing Unit"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter"],
        "answer": "B"
    }
]

score = 0

for item in questions:
    print(item["question"])
    for choice in item["choices"]:
        print(choice)

    user_answer = input("Your answer (A, B, C): ").strip().upper()
    if user_answer == item["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. The correct answer was {item['answer']}.\n")

print(f"You got {score} out of {len(questions)} correct!")