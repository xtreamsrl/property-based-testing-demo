import hypothesis
import pytest
from hypothesis import given, settings
import hypothesis.strategies as st


def gcd(n, m):
    """Compute the Greater Common Divisor of two integers by Euclid's algorithm."""
    n, m = abs(n), abs(m)
    n, m = min(n, m), max(n, m)

    while m % n:
        n, m = m % n, n
    return n


# def test_gcd():
#      # Arrange
#      inputs = [(15, 6), (15, 5), (-9, 15)]
#      expected_res = [3, 5, 3]
#
#      for (n, m), res in zip(inputs, expected_res):
#          # Act
#          d = gcd(n, m)
#          # Assert
#          assert d == res


# def test_gcd_pbt():
#     inputs = [(15, 6), (15, 5), (-9, 15)]
#
#     for (n, m) in inputs:
#         d = gcd(n, m)
#
#         assert d > 0  # d is positive
#         assert n % d == 0  # d divides n
#         assert m % d == 0  # d divides m
#
#         # no other number larger than d divides both n and m
#         for i in range(d + 1, min(n, m)):
#             assert (n % i) or (m % i)
#
#
@given(st.integers(), st.integers())
@settings(max_examples=200)
def test_gcd_pbt_given(n, m):
   d = gcd(n, m)

   assert d > 0  # d is positive
   assert n % d == 0  # d divides n
   assert m % d == 0  # d divides m

   # no other number larger than d divides both n and m
   for i in range(d + 1, min(n, m)):
       assert (n % i) or (m % i)


# DEMO SAVER
# def gcd(n, m):
#     """Compute the GCD of two integers by Euclid's algorithm."""
#     n, m = abs(n), abs(m)
#     n, m = min(n, m), max(n, m)
#
#     if n == 0:
#         return m
#
#     while m % n:
#         n, m = m % n, n
#     return n
#
#
# def test_gcd():
#     # Arrange
#     inputs = [(15, 6), (15, 5), (-9, 15)]
#     expected_res = [3, 5, 3]
#
#     for (n, m), res in zip(inputs, expected_res):
#         # Act
#         d = gcd(n, m)
#         # Assert
#         assert d == res
#
#
# def test_gcd_pbt():
#    inputs = [(15, 6), (15, 5), (-9, 15)]
#
#    for (n, m) in inputs:
#        d = gcd(n, m)
#
#        assert d > 0  # d is positive
#        assert n % d == 0  # d divides n
#        assert m % d == 0  # d divides m
#
#        # no other number larger than d divides both n and m
#        for i in range(d + 1, min(n, m)):
#            assert (n % i) or (m % i)
#
#
# @given(st.integers(min_value=1, max_value=100),
#       st.integers(min_value=-500, max_value=500))
# def test_gcd_pbt_given(n, m):
#    d = gcd(n, m)
#
#    assert d > 0  # d is positive
#    assert n % d == 0  # d divides n
#    assert m % d == 0  # d divides m
#
#    # no other number larger than d divides both n and m
#    for i in range(d + 1, min(n, m)):
#        assert (n % i) or (m % i)

