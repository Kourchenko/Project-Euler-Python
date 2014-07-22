"""
What is the largest prime factor of the number 600851475143 ?
"""

def test_prime(num):    # Scales logarithmically
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def prime_fact(num):  # Just needs to check if number is divisible by prime, scales linear
    i = 2
    while i <= num:
        if test_prime(i) and num % i == 0:
            print i
        i += 1


# Still needs work; while calculating input, takes while to finish, even after it has found the largest prime factor.
