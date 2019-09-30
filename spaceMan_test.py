
from spaceManSecond import is_guess_in_word
from spaceManSecond import get_guessed_word
from spaceManSecond import is_word_guessed



def test_is_guess_in_word():

    assert is_guess_in_word('s', 'Mohammed') == False
    assert is_guess_in_word('y', 'youth') == True


def test_is_word_guessed():
    assert is_word_guessed('MakeSchool', 'MakeSchool') == True
    assert is_word_guessed('I love', 'you') == False
