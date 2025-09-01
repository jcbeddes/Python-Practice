students = [
    {"name": "Alice", "score": 100},
    {"name": "Timmy", "score": 99},
    {"name": "Jonah", "score": 98},
    {"name": "Corey", "score": 97},
    {"name": "Ben", "score": 96},
    {"name": "Brinley", "score": 95},
    {"name": "Bob", "score": 50},
]

for student in students:
    print(f"{student['name']} scored {student['score']}")

total = 0

for student in students:
    total += student["score"]

average = total / len(students)
print(f"\nAverage score: {average}")