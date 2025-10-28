from wordle_lj2496 import wordle_lj2496
validate_guess = wordle_lj2496.validate_guess
check_guess = wordle_lj2496.check_guess

def test_validate_guess():
    # We start by testing 3 valid inputs
    valid_guess_1 = "hello" # normal 5 letters
    test_valid_1 = validate_guess(valid_guess_1)
    assert test_valid_1 == True, "hello is a valid guess"

    valid_guess_2 = "eeeee" # normal lowercase 5 letters
    test_valid_2 = validate_guess(valid_guess_2)
    assert test_valid_2 == True, "eeeee is a valid guess"
    
    valid_guess_3 = "abcde" # alphabetical 
    test_valid_3 = validate_guess(valid_guess_3)
    assert test_valid_3 == True, "abcde is a valid guess"

    
    # We test something too short and too long
    short = "hi"
    test_short = validate_guess(short)
    assert test_short == False, "hi is too short of a guess, should be false"

    long = "waytoolong"
    test_long = validate_guess(long)
    assert test_long == False, "waytoolong is too long of a guess, should be false"


    # We test something uppercase
    upper = "UPPER"
    test_upper = validate_guess(upper)
    assert test_upper == False, "UPPER is not valid because of caps"

    # We test something non-alphabetic
    na = "123ge"
    test_na = validate_guess(na)
    assert test_na == False, "123ge is not valid cause of numeric chars"

    # We now want to finally test our edge cases
    empty = ""
    test_empty = validate_guess(empty)
    assert test_empty == False, "empty string is not a valid guess"

    noneobj = None
    test_none = validate_guess(noneobj)
    assert test_none == False, "None is not a valid input"

    # Check various different types that are not strings
    integer = 12357
    test_int = validate_guess(integer)
    assert test_int == False, "integers are not a valid input"

    listobj = []
    test_list = validate_guess(listobj)
    assert test_list == False, "lists are not a valid input"

    dictobj = []
    test_dict = validate_guess(dictobj)
    assert test_dict == False, "dicts are not a valid input"


def test_check_guess_basic():
    # check perfect match of "johns" and "johns"
    word1 = "johns"
    word2 = "johns"
    perfect_match = check_guess(word1, word2)
    assert perfect_match == [('j', 'green'), ('o', 'green'), ('h', 'green'), ('n', 'green'), ('s', 'green')]

    
    # check no matches
    word3 = "wlatt"
    no_match = check_guess(word2, word3)
    assert no_match == [('w', 'gray'), ('l', 'gray'), ('a', 'gray'), ('t', 'gray'), ('t', 'gray')]

    
    # check some mixed results
    word4 = "crane"
    word5 = "react"
    mixed_1 = check_guess(word4, word5)
    assert mixed_1 == [('r', 'yellow'), ('e', 'yellow'), ('a', 'green'), ('c', 'yellow'), ('t', 'gray')]

    word6 = "hello"
    word7 = "lemon"
    mixed_2 = check_guess(word6, word7)
    assert mixed_2 == [('l', 'yellow'), ('e', 'green'), ('m', 'gray'), ('o', 'yellow'), ('n', 'gray')]


    # check the edge case (lengths not aligning)
    word8 = ""
    word9 = "a"
    edge1 = check_guess(word8, word9)
    assert edge1 == []

    word10 = "asdfg"
    word11 = "asdfgg"
    edge2 = check_guess(word10, word11)
    assert edge2 == []