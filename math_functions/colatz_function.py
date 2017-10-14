
def collatz(start,print_numbers):

    if print_numbers:
        print(start)

    total=start
    chain_length=1
    while total != 1:
        if total%2 == 0:
            total/=2
        else:
            total=total*3+1
        if print_numbers:
            print(total)
        chain_length+=1
    if print_numbers:
        print(("Chain Length: {}").format(chain_length))

    return chain_length

if __name__=="__main__":
    collatz(300,True);