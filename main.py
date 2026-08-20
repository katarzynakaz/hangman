import random
from lives import live_stages
from hangman_words import word_list 
import validate_guess

chosen_word = random.choice(word_list)

placeholder = ''

lives = 6

for index in range(len(chosen_word)):
    placeholder += '_'

guessed_letters = []
game_over = False
print(placeholder)

while not game_over:
    guess = validate_guess()
    display = '' 

    for letter in chosen_word: 
        if letter == guess:
            display += letter
            guessed_letters.append(letter)
        elif letter in guessed_letters:
            display += letter
        else: 
            display += '_'
            
    if guess in guessed_letters:
        print(f'You have already guessed {guess}')
    print(display)

    if guess not in chosen_word:
        lives -= 1 
        print(live_stages[lives])
        print(f"You guessed {guess}, it is not in the word. ****************************{lives}/6 LIVES LEFT****************************")

        if lives == 0:
            game_over = True
            print(f'Game over. The correct word was {chosen_word}')
   
    if '_' not in display:
        game_over = True
        print('You win!')
        


