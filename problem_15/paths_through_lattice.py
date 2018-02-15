from math_functions import combinatorials as c

def paths_through_lattice(target_x,target_y):
    #paths through a lattice are defined as binomial expansion of (n+k n)
    #where n,k is the x,y coordinates of the target point
    #binomial expansion is the same as nCr
    return c.nCr( target_x+target_y, target_x )

if __name__=="__main__":
    print paths_through_lattice(20,20)