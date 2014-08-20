collect = []


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True


for i in range(100, 1000):
    for j in range(100, 1000):
        x = i * j
        if is_palindrome(x):
            collect.append(x)
            collect.sort()

print collect[-1]
