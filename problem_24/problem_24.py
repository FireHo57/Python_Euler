from itertools import permutations as p

def main():

    nums = list(range(0, 10))
    nums = list(p(nums))
    print len(nums)
    nums.sort()
    print(''.join(str(e) for e in nums[1000000-1]))


if __name__ == "__main__":
    main()