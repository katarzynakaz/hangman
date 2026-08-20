def validate_guess(guessed_letters):
    guess = input('Guess a letter\n').lower().strip()
    
    while len(guess) != 1 or not guess.isalpha() or guess in guessed_letters:

        if guess in guessed_letters:
            print(f'You have already guessed {guess}')
        elif len(guess) != 1 or not guess.isalpha():
            print('Please type in only one letter.')

        guess = input("Guess a letter\n").lower().strip()

    return guess