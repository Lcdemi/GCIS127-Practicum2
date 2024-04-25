from practicum import *

"""
As you solve each problem, uncomment the corresponding tests so that you can
verify that your solution works.

Hint: Select the test and press CTRL-/ (or Command-/ on Mac) to toggle the 
comment block.
"""

def test_ascii_tuple_empty():
    # setup
    word = ""
    expected = ()

    # invoke
    actual = ascii_tuple(word)

    # analyze
    assert expected == actual

def test_ascii_tuple_a():
    # setup
    word = "a"
    expected = (97,)

    # invoke
    actual = ascii_tuple(word)

    # analyze
    assert expected == actual

def test_ascii_tuple_dog():
    # setup
    word = "dog"
    expected = (100, 111, 103)

    # invoke
    actual = ascii_tuple(word)

    # analyze
    assert expected == actual

def test_ascii_tuple_dog():
    # setup
    word = "HeRmIoNe!"
    expected = (72, 101, 82, 109, 73, 111, 78, 101, 33)

    # invoke
    actual = ascii_tuple(word)

    # analyze
    assert expected == actual

def test_contains_all_both_empty():
    # setup
    a = []
    b = []
    expected = True

    # invoke
    actual = contains_all(a, b)

    # analyze
    assert expected == actual

def test_contains_all_1_1():
    # setup
    a = [1]
    b = [1]
    expected = True

    # invoke
    actual = contains_all(a, b)

    # analyze
    assert expected == actual

def test_contains_all_1_2():
    # setup
    a = [1]
    b = [2]
    expected = False

    # invoke
    actual = contains_all(a, b)

    # analyze
    assert expected == actual

def test_contains_all_12_12122():
    # setup
    a = [1, 2]
    b = [1, 2, 1, 2, 2]
    expected = True

    # invoke
    actual = contains_all(a, b)

    # analyze
    assert expected == actual

def test_fish_sort_empty():
    # setup
    original = []
    expected = []

    # invoke
    actual = fish_sort(original)

    # analyze
    assert actual is not original
    assert actual == expected

def test_fish_sort_one():
    # setup
    original = [2]
    expected = [2]

    # invoke
    actual = fish_sort(original)

    # analyze
    assert len(actual) == len(original) 
    assert actual is not original
    assert actual == expected

def test_fish_sort_more():
    # setup
    original = [3, 2, 1, 5, 7, 6, 1]
    expected = [1, 1, 2, 3, 5, 6, 7]

    # invoke
    actual = fish_sort(original)

    # analyze
    assert len(actual) == len(original)
    assert actual is not original
    assert expected == actual

def test_phonetic_translation_empty():
    # setup
    a_string = ""
    expected = []

    # invoke
    actual = phonetic_translation(a_string)

    # analyze
    assert expected == actual

def test_phonetic_translation_one_letter():
    # setup
    a_string = "q"
    expected = ["Quebec"]

    # invoke
    actual = phonetic_translation(a_string)

    # analyze
    assert expected == actual

def test_phonetic_translation_one_word():
    # setup
    a_string = "LOVE"
    expected = ["Lima", "Oscar", "Victor", "Echo"]

    # invoke
    actual = phonetic_translation(a_string)

    # analyze
    assert expected == actual

def test_phonetic_translation_two_words():
    # setup
    a_string = "tOp GuN"
    expected = ["Tango", "Oscar", "Papa", "Golf", "Uniform", "November"]

    # invoke
    actual = phonetic_translation(a_string)

    # analyze
    assert expected == actual

def test_phonetic_translation_punctuation():
    # setup
    a_string = "a.b!c-a@"
    expected = ["Alpha", "Bravo", "Charlie", "Alpha"]

    # invoke
    actual = phonetic_translation(a_string)

    # analyze
    assert expected == actual

def test_is_pangram_fox():
    # setup
    a_string = "The quick brown fox jumps over a lazy dog."
    expected = True

    # invoke
    actual = is_pangram(a_string)

    # analyze
    assert expected is actual

def test_is_pangram_jcvd():
    # setup
    a_string = "JCVD might pique a sleazy boxer with funk."
    expected = True

    # invoke
    actual = is_pangram(a_string)

    # analyze
    assert expected is actual


def test_is_pangram_joe():
    # setup
    a_string = "Quick zephyrs blow, vexing daft Joe."
    expected = False

    # invoke
    actual = is_pangram(a_string)

    # analyze
    assert expected is actual