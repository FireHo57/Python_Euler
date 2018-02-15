#problem 16 asks what the sum of the digits of 2^1000
#
if __name__=="__main__":
    total=0
    full_number=str(2**1000)
    for i in full_number:
        total+=int(i)
    print total