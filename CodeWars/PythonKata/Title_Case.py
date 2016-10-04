#!/usr/bin/env python

"""
A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the
first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless
it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The
list of minor words will be given as a string with each word separated by a space. Your function should ignore the case
of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.
Arguments (Haskell)

    First argument: space-delimited list of minor words that must always be lowercase except for the first word in the
    string.
    Second argument: the original string to be converted.

Arguments (Other languages)

    First argument (required): the original string to be converted.
    Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first
    word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.


title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
"""


def upperfirst(x):
    return x[0].upper() + x[1:]


def title_case(cased_title, minor_words=None):
    cased_title = cased_title.title()
    final_phrase = ''
    if not minor_words:
        return cased_title.title()
    else:
        minor_words = minor_words.lower()
        for word in cased_title.split():
            if word.lower() in minor_words:
                final_phrase += word.lower() + ' '
            else:
                final_phrase += word + ' '

    return upperfirst(final_phrase.strip())


def test_function():
    assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
    assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'
    assert title_case('the quick brown fox') == 'The Quick Brown Fox'
    assert title_case('First a of in', 'an often into') == 'First A Of In'

if __name__ == '__main__':
    test_function()
