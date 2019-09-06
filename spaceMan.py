import random

def load_word(): # load_word function is = to a list of guess words
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r') # the open() method opens a file example: worlds.text and "r" print them. in our case it is placed in the f variable.
    words_list = f.readlines() # the readlines method append values into a automatic list.
    f.close() # close method close the words.txt file after the open() method

    words_list = words_list[0].split(" ") # split method seperate every string to individual indexs .
    secret_word = random.choice(words_list) #split() randomize a list and pick a world
    #print(words_list) #print every word in the words_list/word.txt variable
    return words_list



def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check

    #if a letter is not in lettersGuessed
    for word in secret_word:
        if word in letters_guessed:
            print(f"{word} is part of {letter_guessed}")
            return True
        else:
            print(f"{word} is not part of { letter_guessed}")
            return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far
     in the
     secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed
         so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user
        has guessed correctly, the string should contain the letter at the correct
        position.  For letters in the word that the user has not yet guessed,
        shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows
     #the letters that have been guessed correctly so far that are saved in
     #letters_guessed and underscores for the letters that have not been guessed yet
    word_selected_holder = ""
    for letter in secret_word:
        if letter in letter_guessed:
            word_selected_holder += letter + ""
        else:
            word_selected_holder += " _ "

    return word_selected_holder


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
    # Needs more work ( logic seems off)
    for letter in secret_word:
        if letter_guessed in letter:
             return True
        else:
            return False




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman
    in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")
    print ('------------')
    print("The secret word contains: " + str(len(secret_word)) + " letters")


    #TODO: Ask the player to guess one letter per round and check that it is only one letter
def user_input(strin):
    word = strin
    print(word)


user_input(input("Enter a word: "))
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
is_word_guessed(load_word(), get_guessed_word)



    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
