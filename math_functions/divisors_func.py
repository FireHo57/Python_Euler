from prime_finder import sieve_of_e as soe

def divisors_brute_force(target):
    total=0
    for i in range(1,target):
        if target % i == 0:
            total+=1
    return total

def divisors(target,in_primes=[]):
    primes=[]
    if len(in_primes) == 0:
        primes=soe(target)
    else:
        primes=in_primes
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

    num_divisors = 1
    for x in div_list:
        num_divisors *= (len(x)+1)
    return num_divisors


if __name__ == "__main__":
    print divisors(500)