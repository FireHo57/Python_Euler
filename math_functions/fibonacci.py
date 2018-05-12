
# fibonacci is fn = f(n-1) + f(n-2)
def fibonacci(limit):
    sequence=[1,1]
    for x in range(2,limit):
        sequence.append(sequence[x-1]+sequence[x-2])
    return sequence
