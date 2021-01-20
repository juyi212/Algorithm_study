import sys

max_cnt = 100

def check(start, end):
    global max_cnt
    for i in range(end[0], start[0], -1):
        for j in range(end[1], start[1], -1):
            if max_cnt >= (i-start[0])*(j-start[1]):
                continue
            sig = True
            for k in range(start[0], i):
                for m in range(start[1], j):
                    if board[k][m] == True:
                        continue
                    else:
                        sig = False
                        break
            if sig:
                max_cnt = (i-start[0])*(j-start[1])
                break

board = [[False]*100 for _ in range(100)]
T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = True

for i in range(100):
    for j in range(100):
        if board[i][j] == True:
            for k in range(i, 100):
                if board[k][j] != True:
                    break
            for m in range(j, 100):
                if board[i][m] != True:
                    break
            if max_cnt < (k-i) * (m-j):
                check((i,j), (k,m))
print(max_cnt)