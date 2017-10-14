from math_functions import colatz_function as cf
import matplotlib.pyplot as plt

def main():
    x=[]
    y=[]
    max=0
    max_chain=0
    for i in range(1,1000000):
        chain = cf.collatz(i,False)
        if chain > max_chain:
            max=i
            max_chain=chain
        y.append(chain)
        x.append(i)

    print(("Max chain of {} at {}").format(max_chain,max))
    plt.plot(x, y)
    plt.show()

if __name__=="__main__":
    main()

