sudoku = [
         [5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

grill0 = grill1 = grill2 = grill3 = grill4 = grill5 = grill6 = grill7 = grill8 =  []

def build_reverse(sudoku):
    sudoku_reverse = [[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        for j in range(9):
            sudoku_reverse[j].append(sudoku[i][j])
    return sudoku_reverse

def grill_order(n):
    if (n < 3):
        n = 0
    if (3 < n < 6):
        n = 3
    if (6 < n < 9):
        n = 6
    return n

def build_grill(sudoku, grill, x, y):
    x = grill_order(x)
    y = grill_order(y)
    for i in range(3):
        for j in range(3):
            grill.append(sudoku[i+x][j+y])
    return grill
def build_missing(x, y, sudoku, sudoku_reverse, grill):
    missing=[1,2,3,4,5,6,7,8,9]
    for i in sudoku[x]:
        if i in missing:
            missing.remove(i)
    for i in sudoku_reverse[y]:
        if i in missing:
            missing.remove(i)
    for i in grill:
        if i in missing:
            missing.remove(i)
    return missing

grill=[]
sudoku_reverse = build_reverse(sudoku)
print(build_grill(sudoku, grill, 0, 2))
print(build_missing(0,2,sudoku, sudoku_reverse, grill))

def sudoku_greedy(sudoku,sudoku_reverse):
    grill = []
    for i in range(9):
        for j in range(9):
            if (sudoku[i][j] == 0):
                grill = build_grill(sudoku, grill, i, j)
                missing = build_missing(i,j,sudoku, sudoku_reverse, grill)


#sudoku_greedy(sudoku,sudoku_reverse)
