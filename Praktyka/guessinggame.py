import random

print("---------------------------------")
print("         M7M guessing game! ")
print("---------------------------------")

print("Guess the number of M&Ms and you get lunch on the house!")
print()


mm_count = random.randint(1, 101)
attempt_limit = 5
attempts = 0
while attempts < attempt_limit:
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    print(guess)
    attempts += 1

print("Bye")