import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

    ### YOUR CODE STARTS FROM HERE ###
    
  

# Instructions

#     The computer choose a random word and mark stars for each letter of each word.
word_guess = ('*'*len(word))
guessed_letters = []
while True:
    print('Your word guess:')
    print(word_guess)
    
    letter_guess = input('Guess a letter:')

    if letter_guess in word:
        for index, letter in enumerate(word):
            if letter_guess == letter:
                word_guess[index] = letter

#     Then the player will guess a letter.
#         If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
#         If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
#         The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
#         The player can’t guess the same letter twice.
