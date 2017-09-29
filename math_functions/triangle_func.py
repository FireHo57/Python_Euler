def get_nth_triangle(limit):
    return sum( range(1,limit) )

def get_n_triangles(limit):
    triangles=[]
    total=0

    for x in range(1, limit+1):
        total+=x
        triangles.append(total)

    return triangles

if __name__=="__main__":
    print('Nth triangle number: {}'.format(get_nth_triangle(10)))
    print('First N triangle numbers: {}'.format(get_n_triangles(10)))
