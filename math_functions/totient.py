def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def totient(target):
    totients = range(1, target + 1)
    totients = [x for x in totients if gcd(target, x) == 1]
    return totients


if __name__ == "__main__":
    print(totient(24))


