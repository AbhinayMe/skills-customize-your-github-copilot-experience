# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman game in Python to practice string manipulation, loops, conditionals, and user input. You will create a playable word-guessing game that selects words at random and tracks player progress.

## 📝 Tasks

### 🛠️	Create the Hangman Game Logic

#### Description
Write a Python program that implements the Hangman game. The game should randomly select a word from a predefined list and allow the player to guess letters until they either guess the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a list of at least 5 words
- Display the word as underscores (e.g., `_ _ _ _`) and update as correct letters are guessed
- Accept single-letter guesses from the user
- Track and display the number of incorrect guesses remaining
- End the game with a win message if the word is guessed, or a lose message if attempts run out

**Example:**
```plaintext
Word: _ _ _ _ _
Guesses left: 6
Guess a letter: a
Word: _ a _ _ _
Guesses left: 6
...
Congratulations! You guessed the word: magic
```

### 🛠️	Add Replay and Input Validation

#### Description
Enhance your Hangman game by allowing the player to play multiple rounds and by handling invalid input gracefully.

#### Requirements
Completed program should:

- Ask the player if they want to play again after each game
- Validate user input to ensure only single alphabetic characters are accepted as guesses
- Prevent repeated guesses from counting against the player
- Display appropriate messages for invalid or repeated guesses
