# Wordle Game

Wordle is a word guessing game where you have 5 attempts to guess the hidden word. Here are some important details about the game:

- You need to guess a 4-letter word.
- After each guess, you will receive feedback in the form of:
  - (C): A letter is in the correct position.
  - (WP): A letter is in the word but not in the correct position.
  - (NT): A letter is not in the word at all.
- If you guess the word correctly, you win the game!

## Instructions

1. Run the Python code provided in this repository.
2. You will be given 5 attempts to guess the hidden word, which is randomly selected from a list of words.
3. Enter a 4-letter word as your guess.
4. The program will provide feedback on your guess using (C), (WP), and (NT).
5. Keep guessing until you either guess the word correctly or run out of attempts.

## Example

Here's an example of how the game works:

```python
Enter four letter word: pink
(C)(WP)(WP)(NT)
Enter four letter word: cats
(C)(WP)(WP)(NT)
Enter four letter word: help
(C)(WP)(WP)(WP)
Enter four letter word: five
(C)(C)(C)(C)
Congrats! You did it.
