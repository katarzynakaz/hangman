import random
from lives import live_stages
from hangman_words import word_list 
from validator import validate_guess
from update_display import update_display

chosen_word = random.choice(word_list)

placeholder = '_'* len(chosen_word)

lives = 6

guessed_letters = []
invalid_guessed_letters = []

game_over = False
print(placeholder)

while not game_over:
    guess, display = update_display(chosen_word, guessed_letters, invalid_guessed_letters)
            
    print(display)

    if guess not in chosen_word and guess not in invalid_guessed_letters:
        lives -= 1 
        invalid_guessed_letters.append(guess)
        print(live_stages[lives])
        print(f"You guessed {guess}, it is not in the word. ****************************{lives}/6 LIVES LEFT****************************")

        if lives == 0:
            game_over = True
            print(f"Game over. The correct word was '{chosen_word}'")
   
    if '_' not in display:
        game_over = True
        print('You win!')
        


