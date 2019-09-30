import random
import string
from random import shuffle



words_of_encouragement = ["Nice !!", "Dope 👏🏾", "Awesome !!", "You is on fire 🔥", "Ok check you out", 'Lit 🔥']



def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') # comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    # Function was created with the help of Samir Ingle
    counter = 0

    for letter in letters_guessed:
        number_of_letters = secret_word.count(letter)
        if (number_of_letters > 0):
            counter += number_of_letters

    if len(secret_word) == counter:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    letterWord = " "
    # Function was created with the help of Samir Ingle
    for letter in secret_word:
            if letter in letters_guessed:
                letterWord += (letter + " ")
            else:
                letterWord += ("_ ")
    return letterWord


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    for letter in secret_word:
       if (guess == letter):
            return True
    return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    chances = 7
    letters_guessed = []
    #print(secret_word) #uncomment this to see secret word as you play.

    #TODO: show the player information about the game according to the project spec
    print(f'''
    Welcome to Space 🚀 Man.
    you've got {(len(secret_word))}  guesses. buckle up & Good luck!''')

    get_guessed_word(secret_word, letters_guessed)


    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    while (is_word_guessed(secret_word, letters_guessed) == False and chances > 0):

        guess = input('Guess a letter \n')
        print('')


    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
                    #Error handling
        if len(guess) != 1: #making sure user enter something
            print("dude really 🙄?  come on man enter something!! ")
            if guess != "": # making sure the input is a string
                print("lmao you think you is slick, please enter a letter!")

        elif guess in letters_guessed:
            print(f'''Enter something else son, You already guessed "{guess}" !''')

        elif is_guess_in_word(guess, secret_word) is True:
            letters_guessed.append(guess)
            shuffle(words_of_encouragement)
            print(words_of_encouragement[0])
            get_guessed_word(secret_word, letters_guessed)

        elif is_guess_in_word(guess, secret_word) is False:
            print(f"Sorry {guess} is not in the word")

        else:
            chances = chances - 1
            print(f'''Sorry letter "{guess}" is not in the word! You have  {(chances)} chances left''')
            get_guessed_word(secret_word, letters_guessed)


    #TODO: check if the game has been won or lost

    if chances == 0:
        print(f"YOU LOST ❌!!!.  the word you could'nt guess is {(secret_word)}")
    else:
        print(f"Congratulation 🥳. YOU WON.")



#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)





# #These function calls that will start the game
