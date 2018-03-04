#Problem 20 -
# d(n) = sum of proper divisors of n
# if d(a) = b and d(b) = a and a != b then a and b are amicable pairs
# find amicable numbers under 10000
from math_functions import divisors_func as df
from itertools import chain
def main():
    numbers_and_sums=[0]*10000
    # start with an array of zeros
    divisors= df.divisors(10000)[1]

    print sum(chain(*divisors))




    #for i in range (2,10001):
    #    df.divisors(i)
    #    div_sum = (df.divisors(i))
    #    numbers_and_sums.append(i,div_sum)
    #print numbers_and_sums


if __name__=="__main__":
    main()