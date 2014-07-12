"""
Find the sum of the even valued Fibonacci numbers, who are less than 4 million.
"""
y = [0, 1] # Used for even_fib(), helps with running-time.

def fib(n):     # Makes list of Fibonacci Sequence; scales logarithmically.
    x = [0, 1]  # Helps with running-time. Given.
    i = 0
    while i < n:
        a = x[i]
        b = x[i+1]
        x.append(a+b)
        y.append(a+b)
        i += 1
    return x


def even_fib(inp):  # Finds the sum given a list input; scales linear.
    i = 3           # Not even number until 3rd digit in list.
    total = 0
    while i < len(inp) and inp[i] < 4000000:
        if inp[i] % 2 == 0:
            total += inp[i]
        i += 1
    return total
