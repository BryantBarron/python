#hangman game
import random

word_list = ["everquest", "futurama", "league", "yellowstone", "mammoth"]

game_word = random.choice(word_list)

print("Welcome to hangman.\n")

word = []
correct_guesses = []
incorrect_guesses = []
guess = ""
filled_word = []

for char in game_word:
    word += char
    filled_word += "_"

print(game_word)
print(word)
print(filled_word)
    

while(len(incorrect_guesses) <= 5):
    guess = input("Guess a letter: ") 

    while((guess.isalpha() != True)):
        print("You must pick a letter.")
        guess = input("Guess a letter: ")

    guess = guess.lower()

    if guess in game_word:
        print("The letter you guessed is in the word!")
        correct_guesses += guess
        for position in range(len(word)):
            i = word[position]
            if i == guess:
                filled_word[position] = i
                
        print(filled_word)
    else:
        print("The letter you guessed is NOT in the word!")
        incorrect_guesses += guess
        
        


