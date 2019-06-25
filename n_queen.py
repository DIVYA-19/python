def isValid(grid,x,y,n):
    rowCheck = all([grid[x][j] != 1 for j in range(n)])
    colCheck = all([grid[j][y] != 1 for j in range(n)])
    if not rowCheck or not colCheck:
        return False
    i = x+1
    j = y+1
    while(i<n and j<n):
        if grid[i][j] != 1:
            i += 1
            j += 1
        else:
            return False
    i = x-1
    j = y-1
    while(i>=0 and j>=0):
        if grid[i][j] != 1:
            i -= 1
            j -= 1
        else:
            return False

    return True

def Queen(grid,row,n):
    for i in range(0,n):
        if isValid(grid,row,i,n):
            grid[row][i] = 1
            if row==n-1:
                return True
            result = Queen(grid,row+1)
            if result:
                return True
            grid[row][i] = 0
    return False

grid = []
for i in range(n):
    grid.append([0]*n)
    
if Queen(grid,0,n):   
    print(grid)
                
    
