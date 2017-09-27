def divisors(target):
    total=0
    for i in range(1,target):
        if target % i == 0:
            total+=1
    return total