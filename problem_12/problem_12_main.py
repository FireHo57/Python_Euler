from math_functions import triangle_func as tf
from math_functions import divisors_func as df
from math_functions import prime_finder as pf

import matplotlib.pyplot as plt

import time as t

def main():

    # would like to get an idea of how divisors increase with triangle number
    t1=t.time()
    primes=pf.sieve_of_e(100000)
    triangles=tf.get_n_triangles(100000)
    print(tf.get_nth_triangle(100000))
    x_axis=[]
    y_axis=[]
    x_axis.append(1)
    y_axis.append(0)
    for x in triangles[1:]:
        x_axis.append(x)
        y_axis.append(df.divisors(x,primes))

    t2=t.time()
    print(t2-t1)
    plt.plot(x_axis,y_axis)
    plt.show()

if __name__ =="__main__":
    main()