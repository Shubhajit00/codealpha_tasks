import random

def hangman_game_with_clue():
    # Dictionary of words and their clues (categories)
    word_clues = {
        "pizza": "It's a type of food 🍕",
        "mountain": "It's a nature-related thing ⛰️",
        "jacket": "It's a type of clothing 🧥",
        "tiger": "It's an animal 🐅",
        "sofa": "It's a piece of furniture 🛋️"
    }

    # Randomly select a word and its clue
    word = random.choice(list(word_clues.keys()))
    clue = word_clues[word]

    guessed_letters = []
    attempts = 6
    word_display = ['_'] * len(word)

    print("🎮 Welcome to Hangman gamet!")
    print(f"Clue: {clue}")
    print("You have 6 incorrect guesses allowed.")

    while attempts > 0 and '_' in word_display:
        print("\nWord:", ' '.join(word_display))
        print("Guessed letters:", ', '.join(guessed_letters))
        print(f"Attempts remaining: {attempts}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            print("❌ Wrong guess.")
            attempts -= 1

    if '_' not in word_display:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n😞 Out of attempts! The word was:", word)

# Run the game
hangman_game_with_clue()

