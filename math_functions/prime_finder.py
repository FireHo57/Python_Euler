def sieve_of_e(target):

    sieve_list = range(2,target)

    #set initial conditions
    p = sieve_list[0]
    mark = sieve_list[p]

    while p < target:
        print (p)
        while 1:

            try:
                sieve_list[mark] = 0
            except:
                break
            print ('mark: {}'.format(mark))
            mark+=p

        # increment p - it's the next non zero number
        p = next( x for x in sieve_list if x!= 0 and x >= p )
        mark = [sieve_list.index(p)+p]


    return [i for i,e in enumerate(sieve_list) if e!= 0]