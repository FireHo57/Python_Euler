from utility import file_reader as fr

def main():
    num_array = fr.read_to_array('numbers.txt')

    sum = 0
    for x in num_array:
        sum+= int(x)

    print sum




if __name__ == "__main__":
    main()