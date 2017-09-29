from prime_finder import sieve_of_e as soe

def divisors_brute_force(target):
    total=0
    for i in range(1,target):
        if target % i == 0:
            total+=1
    return total

def divisors(target):
    primes = soe(target)
    div_list = []
    total = target
    x = 0

    print("Initial total: {}".format(total))

    while x < len(primes):
        sub_list = []
        while total % primes[x] == 0:
            total /= primes[x]
            print(("total: {}").format(total))
            sub_list.append(primes[x])

        if len(sub_list) != 0:
            div_list.append(sub_list)
        x += 1

    print div_list
    num_divisors = 1
    for x in div_list:
        num_divisors *= x[0] * len(x)
    return num_divisors


if __name__ == "__main__":
    print divisors(500)