# Word Guessing Game with python

# Introduction: One popular game is where we guess an unknown word or phrase one letter at a time. 

# Create the World Bank

import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi', 'instagram', 'facebook', 'vsco']

word = random.choice(word_bank) # randomly select a word from the word_bank list and to assign to the word variable

#Finishing the Set Up

guessedWord = ['_'] * len(word) # multiplying a list by an integer and the list will repeat that amount of time ['_'] creates a list with a single underscore element

attempts = 10

# Game Loop

while attempts > 0:
   
    print('\nCurrent word: ' + ' '.join(guessedWord))

    guess = input('Guess a letter: ').lower()
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break

if attempts == 0:
    print('\nYou\'ve run out of attempts! The word was: ' + word)
    
    

  






