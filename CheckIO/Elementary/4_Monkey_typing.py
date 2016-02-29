#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def count_words(text, words):
    ret_list = 0
    for w in words:
        if re.findall(w.lower(), text.lower()):
            ret_list += 1
    return ret_list


def test_function():
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"


if __name__ == '__main__':
    test_function()