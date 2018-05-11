from math_functions import divisors_func as df
from collections import OrderedDict
import timeit as t

def amicable_numbers(target):
    index = []
    for i in range(1, target+1):
        index.append((i, sum(df.proper_divisors(i))))

    results = []
    for u in index:
        # print("{}".format(u))
        div = "-"
        if u[1] < target:
            div = index[u[1] - 1]

            if div[1] == u[0] and div[0] != u[0]:
                results.extend(div)

    cleaned_results = []
    for i in results:
        if i not in cleaned_results:
            cleaned_results.append(i)

    return cleaned_results

if __name__ == "__main__":
    # amicable_numbers(10)
    print( sum(amicable_numbers(10000)) )