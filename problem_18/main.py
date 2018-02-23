from utility import file_reader as fr

def str_to_int_arrays(input_array):
    output_array = []
    for line in input_array:
        sub = []

        str_array = line.split(" ")
        for i in str_array:
            sub.append(int(i))

        output_array.append(sub)

    return output_array

# assumes that arrays are either square or if triangular then longer rows are at a lower index
def get_highest_adjacent(row,column,array):
    #the two adjacents will be the row below and same column and row below and column +1
    adj1 = array[row-1][column]
    adj2 = array[row-1][column+1]
    return max(adj1,adj2)

def create_weighted_array(int_array):

    weighted_array=int_array[:]
    weighted_array.reverse()

    for i in range (1,len(weighted_array)):
        for j in range (len(weighted_array[i])):
            weighted_array[i][j]+=get_highest_adjacent(i,j,weighted_array)

    return weighted_array


def main():
    array = fr.read_to_array("test_data.txt")

    int_array = str_to_int_arrays(array)
    new_array = create_weighted_array(int_array)
    for i in new_array:
        print i


if __name__ == "__main__":
    main()
