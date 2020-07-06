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
    attempts += 1

    if mm_count == guess:
        print(f"You got a free lunch! It was {guess}.")
        break
    elif mm_count > guess:
        print("Sorry, this's too LOW!")
    else:
        print("That's too HIGH!")


if attempts == 5:
    print(f"Game Over \n Bye , you're done in {attempts}! \n corect is {mm_count}")
else:
    print(f"Bye, you're done in {attempts}!")
