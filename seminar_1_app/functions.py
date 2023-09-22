from random import randint


def random_cube():
    return randint(1, 6)


def random_digit():
    return randint(0, 100)


def heads_and_tails():
    if randint(0, 1) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(random_cube())
