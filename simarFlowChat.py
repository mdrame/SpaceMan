from random import choice
#import random
#random.seed()



#"rat", "dog", "lap", "sat" # reserve words

listt = ["cat"]



after_list_is_randomize = listt[0]
user_guessed_letter = list()
choice(after_list_is_randomize)

def user_input(askUser):
    user_answer = askUser
    return user_answer



user_guessed_word = str(user_input(input("Pls Enter a letter: ")))
secret_letters_list = list(after_list_is_randomize) # secretword is not = listt
print(secret_letters_list)


def useInput_secretWord_list():
    user_guess_letter = str(user_input(input("Pls Enter a letter: ")))
    secret_letters_list = list(after_list_is_randomize) # secretword is not = listt
    is_guess_in_word(secret_letters_list,user_guess_letter)
    #print(secret_letters_list) # <!--- Test --->

    return user_guess_letter





def is_guess_in_word(secret_letter_list, user_guessed_letter):

        if user_guessed_letter in secret_letter_list:
            print(f"Letter  {user_guessed_letter} is in listt {secret_letter_list}")
            blank = list() #printing "_" for the length of secret_word
            count = 0

            for i in secret_letter_list:
                if i in  user_guessed_letter:
                    blank.append(i)
                else:
                    blank.append("")

            print(blank)
            return True
        elif user_guessed_letter not in secret_letter_list:
            print(f"Letter  {user_guessed_letter} is not in listt {secret_letter_list}")
            wrong_guess_word()
            return False





def wrong_guess_word():

    blank = ["-"]*len(secret_letters_list) #printing "_" for the length of secret_word
    print(blank)
    #for i in range(len(user_guessed_letter)):
    #user_guess_letter_turn_into_a_word = "cat" # need a right location
    #user_guess_letter_turn_into_a_word += user_guessed_letter +  " "
    #print(user_guess_letter_turn_into_a_word)
    useInput_secretWord_list()
    is_guess_in_word(secret_letters_list, user_guessed_word)


def guess_complete():
    pass






is_guess_in_word(secret_letters_list, user_guessed_word)
