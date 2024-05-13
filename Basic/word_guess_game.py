import os

print("Guess the Word: A Two Player Game")
while True:
    word = input("Enter the Word : ")
    if word:
        hint = input("Enter the Hint (Please Enter to Skip): ")
        break
    else:
        print("Please enter a valid word")
os.system("cls")   # clear the screen for the second player (above basic level)
guess_count = 3
while guess_count > 0:
    guess = input(f"Guess the Word ({guess_count} remaining): ")
    if guess == word:
        print("Congratulations! You've guessed the word.")
        break
    elif guess_count == 2 and hint:
        print("Here's the Hint : " + hint)
    elif not guess:
        print("Please enter a word !!")
        guess_count += 1
    elif guess != word :
        print("Sorry! Wrong Word.")
    guess_count -= 1
else:
    print(f"You've Failed to Guess the Word : {word}")
