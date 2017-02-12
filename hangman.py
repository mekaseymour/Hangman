import time
from random import randint

# set list of words to guess in the game
words_to_guess = ['antelope', 'elephant', 'giraffe', 'chameleon', 'groundhog']

spaces = []

# number of lives, one for the head, each arm, each leg, and the body
number_of_lives = 6

# randomly select which word to choose
random_number = randint(0, len(words_to_guess)-1)
word_to_play = words_to_guess[random_number]
print(word_to_play)

# start the game
print("Let's play HANGMAN (animal edition)!")
time.sleep(.8)

# print the initial spaces
for letter in range(len(word_to_play)):
    spaces.append('_ ')

print(*spaces, sep='')
print("\n")

# ask the user for their first guess
user_guess = input('Guess a letter: ')

# iterate through the users tries
while number_of_lives > 0:
    if user_guess in word_to_play:
        #print("you're right")

        # find places for occurences of user guess in word
        places = [i for i in range(len(word_to_play)) if user_guess == word_to_play[i]]

        # replace the appropriate spaces with the user's guessed letter
        for number in places:
            spaces[number] = user_guess

        print(*spaces, sep='')
        print("\n")

        # check for win
        if '_ ' not in spaces:
            print('YOU WIN!!!')
            break

        user_guess = input('Guess a letter: ')

    else:
        print("Try again!")
        print("\n")
        number_of_lives -= 1
        user_guess = input('Guess a letter: ')

# if user has no more lives, print 'you lose'
if number_of_lives == 0:
    print('YOU LOSE!!!')
