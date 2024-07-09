print("Enter the number of Queens: ")
N=int(input())
board=[[0]*N for _ in range(N)]

def N_Queens(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not isattack(i,j) and board[i][j]!=1):
                board[i][j]=1
                if N_Queens(n-1) == True:
                    return True
                board[i][j]=0
    return False

def isattack(i,j):
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for l in range(0,N):
        for m in range(0,N):
            if (l+m==i+j) or (l-m==i-j):
                if board[l][m]==1:
                    return True
    return False

N_Queens(N)
for i in board:
    print(i)