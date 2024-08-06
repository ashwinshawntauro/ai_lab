print("Enter the number of queens: ")
n=int(input())
board = [[0]*n for _ in range(0,n)]
def attack(i,j):
    for k in range(n):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(n):
        for l in range(n):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True

def n_queens(n):
    if n==0:
        return True
    for i in range(0,n):
        for j in range(0,n):
            if (not attack(i,j) and board[i][j]!=1):
                board[i][j]=1
                if n_queens(n-1):
                    return True
            board[i][j]==0
    return False

n_queens(n)
for i in board:
    print(i)
