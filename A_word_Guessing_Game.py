import random

#hangman stick figure stages
hangman_stages = [
    """
       ______
       |    |
       |    
       |    
       |    
       |    
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |    
       |    
       |    
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |    |
       |    
       |    
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |   /|
       |    
       |    
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |   /|\\
       |    
       |    
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |   /|\\
       |   /
       |    
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |   /|\\
       |   / \\
       |    
    ___|___
    """
]



#list of words that can be answer 

word_bank =['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi',  "apple", "ball", "tree", "book", "fish", "gold", "milk", "rain", "star", "door",
    "cake", "frog", "wolf", "king", "moon", "ship", "road", "fire", "lake", "rose",
    "bird", "home", "nest", "ring", "farm", "play", "jump", "duck", "goat", "lamp",
    "wind", "sand", "snow", "leaf", "seed", "pear", "corn", "wood", "lock", "bear",
    "lion", "cake", "gift", "shoe", "soap", "sock", "card", "ball", "kite", "frog"
]

#now to randomly choose one of these to be correct answer

word = random.choice(word_bank)

#now we need to show empty underscores or spaces for the word it is before without revealing so we will use underscore as placeholders and multiply with length of word that is chossed by module
guessWords = ['_'] * len(word)

#no of attempt player has ṇ

attempts = 6
wrong_guesses = 0
guessed_letters =[]
#game loop

print("Welcome to Hangman!")
print("Try to guess the word before the hangman is complete!")

while wrong_guesses<attempts:
        print(hangman_stages[wrong_guesses])
        
        print('\nCurrent Word:' + ' '.join(guessWords))
        print('\n Guessed letters:' + ''.join(guessed_letters))
        print('Wrong Guesses:' + str(wrong_guesses) + '/' + str(attempts))
        
        guess = input('Guess a Letter for Word: ').lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        #check if input is valid (single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single letter!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
          for i in range(len(word)):
            if word[i]==  guess:
              guessWords[i] = guess
            print('Great guess!')
        else:
          wrong_guesses +=1
          print('Wrong Guess! ')
          
        if '_' not in guessWords:
            print("\n Congratulations!!! you Guessed the word: "+ word)
            break

        if wrong_guesses >=attempts and '_' in guessWords:
              print(hangman_stages[attempts])
              print('\nGame Over! You\'ve been hanged!')
              print('The word was: ' + word)

