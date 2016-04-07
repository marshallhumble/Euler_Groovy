def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    end_phrase = ""
    for string in phrases:
        end_phrase += string.replace("right", "left") + ','
    return end_phrase.rstrip(',')


def test_function():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"


if __name__ == '__main__':
    test_function()
