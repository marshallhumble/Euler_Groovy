OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == OPERATION_NAMES[0]:
        return int(x and y)
    if operation == OPERATION_NAMES[1]:
        return int(x or y)
    if operation == OPERATION_NAMES[2]:
        return int(not x or y)
    if operation == OPERATION_NAMES[3]:
        return int(not (x == y))
    return int(x == y)


def test_function():
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"


if __name__ == '__main__':
    test_function()
