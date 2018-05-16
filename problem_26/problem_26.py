

def longest_pattern(num_in_str):

    chain_length = 1
    chain = []

    start_chain=num_in_str[0]
    end_chain=num_in_str[0]


    while 1:
        try:

        except:






def main():
    divs = [1.0/x for x in range(1,1001)]

    # only want fraction bit of it
    divs=[ (str(x-int(x))[1:]).split('.')[1] for x in divs ]
    print(divs)


if __name__ == "__main__":
    main()