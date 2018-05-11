from utility import file_reader as fr
from operator import mul


def main():
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    arr = fr.read_to_array("names.txt", ',')
    arr = [ x.replace("\"", "") for x in arr]
    arr.sort()

    print(arr.index("COLIN"))
    print(arr.index("CHARLIE"))
    arr = [mul( sum([alpha.index(x)+1 for x in y]) , i+1 ) for i,y in enumerate(arr)]

    print sum(arr)

if __name__ == "__main__":
    main()
