import random

words = ['royal', 'challengers', 'bengaluru', 'virat', 'kohli', 'runmachine', 'hangman']

def choose_word(words):
    return random.choice(words)

def initialize_game(word):
    guessed_letters = set()
    attempts = 6
    return word, guessed_letters, attempts

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def process_guess(word, guessed_letters, guess):
    guessed_letters.add(guess)
    if guess not in word:
        return False
    return True

def play_hangman():
    print("Welcome to Hangman!")
    word = choose_word(words)
    word, guessed_letters, attempts = initialize_game(word)

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if process_guess(word, guessed_letters, guess):
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    play_hangman()
