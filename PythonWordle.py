import random

words = ["this", "five", "help", "lake", "pink", "cats"]
max_attempts = 5


def check_word(guess):
    if hidden_word == guess:
        print("Congrats! You did it.")
        return True
    else:
        result = ""
        for i, j in zip(guess, hidden_word):
            if i == j:
                result = result + "(C) "
            elif i in hidden_word:
                result = result + "(WP) "
            else:
                result = result + "(NT) "
        print(result)
        return False


def main():
    current_attempt = 1
    while current_attempt <= max_attempts:
        guess = input("Enter four letter word: ")
        if check_word(guess):
            break
        else:
            current_attempt += 1


print('''Wordle is a word guessing game.
You have 5 attempts
(C) Means the letter is in the word and in the correct position,
(WP) means the letter is in the word but not in the correct position, 
(NT) means the letter is not there in the word itself.
Best of luck''')
hidden_word = random.choice(words)

main()
