#!/usr/bin/env python

# An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or
# phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from
# another by rearranging the letters. Anagrams are case-insensitive and don't take account whitespaces. For example:
# "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.
# You are given two words or phrase. Try to verify are they anagrams or not.
# How it is used: Anagramming can be a fun way to train your brain, but they have and another application.
# Psychologists use anagram-oriented tests, often called "anagram solution tasks", to assess the implicit memory.
# Anagrams are connected to pseudonyms, by the fact that they may conceal or reveal, or operate somewhere in between
# like a mask that can establish identity. In addition to this, multiple anagramming is a technique sometimes used to
# solve some kinds of cryptograms.


def verify_anagrams(first_word, second_word):
    return sorted(first_word.replace(" ", "").lower()) == sorted(second_word.replace(" ", "").lower())


def test_function():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"


if __name__ == '__main__':
    test_function()
