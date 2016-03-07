#!/usr/bin/env python

"""
Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession. For example, the string "start 5 one two three 7
end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.
"""


def checkio(words):
    word_count = 0
    for w in words.split(" "):
        if word_count == 3:
            break
        elif w.isalpha():
            word_count += 1
        elif w.isdigit():
            word_count = 0

    if word_count >= 3:
        return True
    else:
        return False


# These "asserts" using only for self-checking and not necessary for auto-testing
def test_function():
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True
    assert checkio("one two 3 four five 6 seven eight 9 ten eleven 12") == False

if __name__ == '__main__':
    test_function()