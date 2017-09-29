import time as t

def sieve_of_e(target, timed=False):
    my_list = range(2, target)
    p = my_list[0]
    mark = p

    primes = []
    primes.append(p)

    t0 = t.time()
    # below while loop will break as soon as next throws an exception
    while 1:

        while mark < target:
            try:
                my_list[mark] = 0
            except:
                # print "Exception!"
                break

            mark += p

        try:
            p = next(x for i, x in enumerate(my_list) if x != 0 and x > p)
            primes.append(p)

            mark = my_list.index(p)
            # print 'mark: {}'.format(mark)
        except:
            break

    t1 = t.time()

    if timed:
        print "Time elapsed: {}".format(t1 - t0)
    return primes


if __name__ == "__main__":
    print sieve_of_e(100)


