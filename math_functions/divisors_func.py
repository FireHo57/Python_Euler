from prime_finder import sieve_of_e as soe


def divisors_brute_force(target):
    total = 0
    for i in range(1, target):
        if target % i == 0:
            total += 1
    return total


def prime_divisors(target, in_primes=[]):
    primes=[]
    if len(in_primes) == 0:
        primes = soe(target)
    else:
        primes = in_primes
    div_list = []
    total = target
    x = 0

    while x < len(primes):
        sub_list = []
        while total % primes[x] == 0:
            total /= primes[x]
            sub_list.append(primes[x])

        if len(sub_list) != 0:
            div_list.append(sub_list)
        x += 1

    return div_list


def count_num_divisors(divisors_list):
    num_divisors = 1
    for x in divisors_list:
        num_divisors *= (len(x) + 1)
    return num_divisors


# returns a list of numbers that are evenly divisible into target
def proper_divisors(target):
    divisors = []
    for i in range(1, target/2 + 1):
        if target % i == 0:
            divisors.append(i)

    return divisors


def all_proper_divisors_below(target):
    divisor_list = []
    for x in range(1, target + 1):
        divisor_list.append(proper_divisors(x))

    return divisor_list


if __name__ == "__main__":
    print proper_divisors(500)
    print( proper_divisors(24) )
