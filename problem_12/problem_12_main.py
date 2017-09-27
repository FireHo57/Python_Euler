from math_functions import triangle_func as tf
from math_functions import divisors_func as df

def main():

    #this will eventually do something
    print("Hello world")
    total = tf.triangle(50000)
    print(total)
    divs = df.divisors(total)
    print(divs)


if __name__ =="__main__":
    main()