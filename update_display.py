from validator import validate_guess

def update_display(chosen_word, guessed_letters, invalid_guessed_letters):
    guess = validate_guess(guessed_letters, invalid_guessed_letters)
    display = '' 

    for letter in chosen_word: 
        if letter == guess:
            display += letter
            guessed_letters.append(guess)
        elif letter in guessed_letters:
            display += letter
        else: 
            display += '_'

    return guess, display