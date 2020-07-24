# Input
import numpy as np
grid = []
print("Give empty spaces as zeros")
for _ in range(9):
    row = list(map(int, input("Row - {}: ".format(_+1)).strip().split()))
    grid.append(row)


# Logic
def possible(x,y,n):
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True

def solve():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1,10):
                    if possible(j, i, num):
                        grid[i][j] = num
                        solve()
                        grid[i][j] = 0
                return
    print("\nYAY!!\n")
    print(np.matrix(grid))


# Calling Solve function
solve()

