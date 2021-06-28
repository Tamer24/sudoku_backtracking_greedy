import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

#grid = [[5,3,0,0,7,0,0,0,0],
#        [6,0,0,1,9,5,0,0,0],
#        [0,9,8,0,0,0,0,6,0],
#        [8,0,0,0,6,0,0,0,3],
#        [4,0,0,8,0,3,0,0,1],
#        [7,0,0,0,2,0,0,0,6],
#        [0,6,0,0,0,0,2,8,0],
#        [0,0,0,4,1,9,0,0,5],
#        [0,0,0,0,8,0,0,0,0]]

def possible(y,x,number):
    global grid
    # Checkea que no exista en la fila
    for i in range(0,9):
        if grid[y][i] == number:
            return False
    # Checkea que no exista en la columna 
    for i in range(0,9):
        if grid[i][x] == number:
            return False
    # Checkea que no exista en la grilla
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    input("More?")

solve()

