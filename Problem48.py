def self_powers(power, to_num):
    total = 0
    for i in range(1, power+1):
        total += i**i

    return str(total)[len(str(total))-to_num:]



def test():
    assert int(self_powers(10, 2)) == 17
    assert int(self_powers(4, 4)) == 8

    assert int(self_powers(1000, 10)) == 9110846700


if __name__ == '__main__':
    test()
