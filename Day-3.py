###discs logic

def disc(n,src,extra,dest):
    if n==1:
        print("Move the",src,"to destination",dest)
        return
    disc(n-1,src,dest,extra)
    print("Move", n, "th disc from", src, "to", dest)
    disc(n - 1, extra, src, dest)
n=int(input())    
disc(n, "source", "extraSpace", "destination")
print("\n\n\n\n\n")


### sudoko layout

def printMatrix(x, y, board):
    if x == 9:
        print("Traversal completed")
        return 
    print(board[x][y], end = " ")
    nextX, nextY = -1, -1 
    if y == 8:
        nextX = x + 1 
        nextY = 0 
        print()
    else:
        nextX = x 
        nextY = y + 1
 
    printMatrix(nextX, nextY, board)
board = []
for i in range(9):
    row = []
    for j in range(1, 10):
        row.append(j)
    board.append(row)
 
printMatrix(0, 0, board)
