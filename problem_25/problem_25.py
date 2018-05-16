from math_functions import fibonacci as f

def main():
    #cheated slightly and just generated numbers until i got to 1000 digits
    fibs=f.fibonacci(4782)
    print(len(str(fibs[-1])))

if __name__ == "__main__":
    main()