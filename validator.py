def validate_guess():
    guess = input('Guess a letter\n').lower().strip()

    while len(guess) != 1 or not guess.isalpha():
        print('Please type in only one letter.')
        guess = input('Guess a letter\n').lower().strip()
    
    return guess