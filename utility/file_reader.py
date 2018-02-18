import os

#reads file (at filePath) contents into string preserving newlines
def read_to_string(filePath):
    targetFile=open(filePath)
    str=''
    x = targetFile.readline()
    while len(x) != 0:
        str+=x
        x = targetFile.readline()
    return str

def read_to_array(filepath):
    targetFile=open(filepath)
    arr=[]
    x = targetFile.readline()
    while len(x) != 0:
        arr.append(x.rstrip())
        x = targetFile.readline()

    return arr

if __name__ == "__main__":
    file = os.path.dirname(__file__)
    print file
    file+="/../problem_13/"
    filename=os.path.join(file,'numbers.txt')

    print(filename)
    print( "read_to_string:\n\n" )
    print(read_to_string(filename))
    print( "read_to_array:\n\n" )
    print(read_to_array(filename))


