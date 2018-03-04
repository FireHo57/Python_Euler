from math_functions import divisors_func as df
from collections import OrderedDict

def amicable_numbers(target):
    search_list=dict()

    for i in range(1,target+1):
        search_list[i]=sum(df.proper_divisors(i))

    # order the list
    ordered_search_list = OrderedDict(search_list)
    # walk through the list following the sum numbers. Only pairs will link to each other

    a = next(iter(reversed(ordered_search_list)))
    b = ordered_search_list.get(a,None)

    while b is not None:
        b = ordered_search_list.get(a, None)
        print("a,b: {},{}".format(a, b))
        if b is None:
            # if b is None then a will have been deleted
            # get a fresh number
            a = next(iter(reversed(ordered_search_list)))
            b = ordered_search_list.get(a, None)
        else:
            if a != b:
                prev_a = a
                prev_b = b
                a = ordered_search_list.get(prev_b, None)
                ordered_search_list.pop(prev_a,None)
                ordered_search_list.pop(prev_b,None)
            else:
                # the values to somewhere..
                print("tbc")


    print(ordered_search_list)




if __name__ == "__main__":
    amicable_numbers(10)