"""

There exists a pythagorean triplet, in which a<b<c and a + b + c == 1000.
Find the product of a*b*c.
"""


def pythagorean_triplet():

    # Given:
      # a !> b
      # c^2 = a^2 + b^2
        # if this holds true, find their sum and if it equals 1000, print all three.
    for a in range(1, 250):
        for b in range(1, 500):
            c = (a**2 + b**2)**0.5
            if a + b + c == 1000:
                if a + b + c:
                    print(a, b, int(c))

def main():
    a, b, c = pythagorean_triplet()
    return a*b*c


if __name__ == '__main__':
    print(main())
