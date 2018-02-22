def sum_numbers(input_array):
    total = 0
    for line in input_array:
        try:
            row = line.split()
            for number in row:
                total += int(number)
        except:
            total = int(line)

    return total


class Position:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def up_x(self):
        self._x += 1

    def up_y(self):
        self._y += 1

    def up_both(self):
        self._x += 1
        self._y += 1

    def x(self):
        return self._x

    def y(self):
        return self._y

    def __str__(self):
        return "[{},{}]".format(self._x,self._y)


# going left and down left-right index doesn't change
def left_total(input_array, position):
    total = 0
    # start on the row below, stay at the same x position
    for row in input_array[position.y() + 1:]:
        total += row[position.x()]
    # for i in range( position._y + 1, len(input_array) -1 ):
    #    total+=input_array[i][position._x]
    return total


def right_total(input_array, position):
    total = 0
    # everytime we follow right we need to increment the x position
    x = position.x() + 1
    for row in input_array[position.y() + 1:]:
        total += row[x]
        x += 1

    return total

def track(input_array):
    # start at the top
    current_position = Position(0, 0)
    current_track = [current_position]
    total = input_array[0][0]
    while current_position.y() < len(input_array) - 1:
        left=left_total(input_array, current_position)
        right=right_total(input_array, current_position)
        print "Left total vs Right total: {} - {}".format(left,right)
        if left > right:
            # go left, x stays the same y increases
            current_position.up_y()
            print "Going left"
        else:
            # go right, x increases y increases
            current_position.up_both()
            print "Going right"
        total += input_array[current_position.y()][current_position.x()]
        print current_position
        current_track.append(current_position)

    print "Total: {}".format(total)
    return current_track


def high_number_array(int_array):
    copy_of_int_array=int_array
    for row in int_array:
        maximum = max(row)
        for i in range(0,len(row)):
            if row[i] < maximum:
                row[i] = 0
            else:
                row[i] = 1
        print row
