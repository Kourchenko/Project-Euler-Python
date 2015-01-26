__author__ == 'Diego'

"""
2520 is the smallest number divisible by all the numbers 1-10.
Find the smallest number divisible by all the numbers 1-20.

Number will be greater than 2520. Number may be multiple of 2520, given that it should be divisible by 1-20.

Theory: Number cannot exceed 1 billion, 1,000,000,000.
"""

def smallest_mult_bruteforce():
    first_solution = 1
    i = 1
    while i <= 10:
        if first_solution % i == 0:
            i += 1
        else:                       # RESET
            i = 1
            first_solution += 1

    second_solution = first_solution

    while i <= 20:
        if second_solution % i == 0:
            i += 1
        else:                       # RESET
            i = 1
            second_solution += first_solution

    return second_solution

print(smallest_mult_bruteforce())





divisible_list = [i for i in range(1, 20)]

def smallest_mult_quickest():
    for number in range(2520, 1000000000, 2520):      
        if all(number%n==0 for n in divisible_list):
            return number
    return None

print(smallest_mult())
