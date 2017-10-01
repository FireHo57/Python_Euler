from utility import file_reader as fr

def main():
    num_array = fr.read_to_array('numbers.txt')

    for x in num_array:
        split_num=[x[i:i+10] for i in range(0 , len(x), 10)]





if __name__ == "__main__":
    main()