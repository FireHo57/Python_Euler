import math as math

def nCr( n , r ):

    if n < r:
        return 0

    # nCr: n!/((n-r)!r!)
    divisor = math.factorial(n)
    print "Divisor: "+str(divisor)
    denominator = math.factorial(n-r)*math.factorial(r)
    print "Denominator: "+str(denominator)
    return divisor/denominator

def nPr( n , r ):
    # nPr: n!/(n-r)!
    divisor = math.factorial(n)
    print "Divisor: "+str(divisor)
    denominator = math.factorial(n-r)
    print "Denominator: "+str(denominator)
    return divisor/denominator

if __name__ == "__main__":
    n=9
    r=4
    print "n: {} r: {}".format(n,r)
    print "nCr: "+str(nCr(n,r))
    print "nPr: "+str(nPr(n,r))