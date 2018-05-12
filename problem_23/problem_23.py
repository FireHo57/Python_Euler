from math_functions import divisors_func as df


def main():
    print("Entering main")
    # step 1 find all abundant numbers below 28123
    divisor_list = df.all_proper_divisors_below(28123+1)
    divisor_list = [sum(x) for x in divisor_list]
    abundant_numbers = [i + 1 for i, num in enumerate(divisor_list) if num > i + 1]

    print("summing")
    can_be_summed = []
    sum_targets = [x for x in abundant_numbers if x < (28124/2)]

    while len(sum_targets) != 0:
        lho = sum_targets[0]
        for rho in sum_targets:
            total = lho + rho
            can_be_summed.append(total)
        sum_targets.pop(0)

    can_be_summed = set(can_be_summed)
    all_numbers = set(range(1, 28124))
    remaining = list(all_numbers - can_be_summed)
    remaining.sort()
    print(remaining)
    print(sum(remaining))

if __name__ == "__main__":
    main()
