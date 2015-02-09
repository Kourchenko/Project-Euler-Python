def test_prime(number):
    base = 2

    if number == 2:
        return 2

    while base < number**0.5+1:
        if number % base == 0:
            return False
        base += 1
    return True


def to_prime(num):

    start = 0
    position = 1

    prime = 2

    while start <= num:
        if test_prime(position):
            prime = position
            start += 1
        position += 1

    return prime
    
    
def test_cases():
  assert to_prime(10001) == 104743
  assert to_prime(10) == 29
  assert to_prime(1) == 2
  assert to_prime(0) == 1
  
