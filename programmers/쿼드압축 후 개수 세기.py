# 분할 정복
def check(x, y, n):
    ch = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != ch:
                check(x, y, n//2)
                check(x, y+n//2, n//2)
                check(x+n//2,y, n//2)
                check(x+n//2,y+n//2, n//2)
                return
    ret.append(ch)


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
ret = []
check(0, 0, len(arr))
anwser = [ret.count(0), ret.count(1)]
print(anwser)