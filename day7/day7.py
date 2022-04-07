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

print(filled_word)
    
print("\n")

end_of_game = False
while not end_of_game:
    guess_count = 0
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
    elif guess in incorrect_guesses:
        print(f"You already guessed: {guess}")
    else:
        print("The letter you guessed is NOT in the word!")
        incorrect_guesses += guess
        print(f"Here are your guesses so far: {incorrect_guesses}")
        if(len(incorrect_guesses) == 5):
            print("You have killed your hangman!")
            end_of_game = True
        
        
        

