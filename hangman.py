import random

# List of 5 predefined words
words = ["python", "apple", "tiger", "laptop", "coding"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("===== Welcome to Hangman Game =====")

while wrong_guesses < max_wrong:

    display = ""

    # Show guessed letters
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Win condition
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_wrong - wrong_guesses)

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)