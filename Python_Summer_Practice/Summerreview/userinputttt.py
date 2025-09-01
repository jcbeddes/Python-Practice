# Stripping spaces

# text = input("Type something with extra spaces: ")
# print(f"Without spaces: '{text.strip()}'")

# Capitalization

# name = input("What's your name boy? ")
# print(f"Proper: {name.capitalize()}")
# print(f"Upper: {name.upper()}")
# print(f"Lower: {name.lower()}")

# Removing leters

# word = input("TELL ME A WORD: ")
# letter = input("What letter do you hate most: ")
# print("Result: ", word.replace(letter, ""))

# Flipping a sequence

# text = input("Tell me another word boi: ")
# print("Reversed: ", text[::-1])

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print("Word list: ", words)
# print("Joined with dashes: ", "-".join(words))

# Checking content

# code = input("Enter a secret code: ")

# if code.isdigit():
#     print("Only digits entered.")
# elif code.isalpha():
#     print("Only letters entered.")
# elif code.isalnum():
#     print("Letters and numbers mixed")
# else:
#     print("Special characters included, IDIOT.")

# Challenge 1: Ask user for input, print all caps version, lowercase, and first name only

# name = input("Tell me your entire full name: ")

# print(f"All caps: {name.upper()}")
# print(f"All lower: {name.lower()}")
# print(f"First name: {name.split()[1]}")

# Challenge 2: Ask the user for a sentence. Reverse the order of the words (not letters).

# sentence = input("Write a senctence: ")

# sentence = sentence.split()
# sentence = sentence[::-1]

# print(f"Reversed: ", " ".join(sentence))

