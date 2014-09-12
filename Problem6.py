__author__ = 'Diego'

"""
Take the sum of the squares of natural numbers; (1^2 + 2^2 + 3^2 + ...).
Take the square of the sum of the natural numbers; (1 + 2 + 3 + ...)^2.
Find the difference in them.

The sum squared grows faster than the squares summed.
"""


def squared_sum(number):
    """ The sum of the squares. """

    i = 1
    total_sum = 0
    while i <= number:
        total_sum += i**2
        i += 1
    return total_sum



def sum_squared(number):
    """ The square of the sum. """

    i = 1
    total_squared = 0
    while i <= number:
        total_squared += i
        i += 1
    return total_squared**2


def test_cases():
    """ Test to prove correct result. """

    assert sum_squared(10) - squared_sum(10) == 2640
    assert sum_squared(100) - squared_sum(100) == 25164150


print test_cases()




