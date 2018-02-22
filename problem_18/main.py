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

def create_weighted_array(int_array):

    weighted_array=int_array
    for i in reversed(weighted_array[0:-1]):
        # for each row add the previously weighted adjacents
        for j,i in enumerate(i):
            print "j: {} i: {}".format(j,i)



def main():
    array = fr.read_to_array("test_data.txt")

    int_array = str_to_int_arrays(array)
    create_weighted_array(int_array)



if __name__ == "__main__":
    main()
