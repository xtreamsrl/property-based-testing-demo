from hypothesis import given
from hypothesis.strategies import text


# https://rosettacode.org/wiki/Run-length_encoding
# Input: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Output: [(12, W), (1, B), (12, W), (3, B), (24, W), (1, B), (14, W)]
def encode(input_string):
    if not input_string:
        return []

    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q


# DEMO SAVER
# @given(text())
# def test_decode_inverts_encode(s):
#     assert decode(encode(s)) == s
