import sys
# 모든거 탐색하면서 백트래킹 해줘야함


def check(x, y, dep):   # 깊이를 이용해서 .... 백트래킹을 넣어주자
    global cnt,num
    if cnt <= dep:
        return

    if matrix[y][x] == 1:
        for k in range(5, 0, -1):
            if 0 < x+k <= 10 and 0 < y+k <= 10 and recheck(x, y, k) and num[k] > 0:
                # recheck 를 했을 때 통과하면 덮을 수 있음
                change(x, y, k, 0)  # 0으로 바꿔주고
                num[k] -= 1 # 종이의 크기 하나 빼준다
                if x < 9:
                    check(x + 1, y, dep+1)
                else:   # x가 9보다 클 때
                    if y < 9:
                        check(0, y + 1, dep+1)
                    else:   # 마지막 종료조건
                        check(x, y, dep+1)
                change(x, y, k, 1)
                num[k] += 1     # 다시 1로 바꾸고 빼줬으면 더해줘야함

    else:
        if x < 9:
            check(x+1, y, dep)
        else:
            if y < 9:
                check(0, y+1, dep)
            else:   # 마지막 종료조건인데, 색종이가 잘 붙어있는지 확인해줘야함
                for n in range(len(matrix)):
                    for m in range(len(matrix)):    # 카운트써도 되겟다 matrix[n].count(1)>0: return
                        if matrix[n][m] == 1:
                            return
                else:
                    cnt = min(cnt, dep)  # dep 깊이 cnt paper 수
                    return


def recheck(x, y, k):
    for i in range(k):
        for j in range(k):
            if matrix[y+i][x+j] != 1:
                return 0
    return 1


def change(x, y, k, value):
    for i in range(y, y+k):
        for j in range(x, x+k):
            matrix[i][j] = value


matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
num = [0, 5, 5, 5, 5, 5]
cnt = 26 # 최대 25장 붙일 수 있어서
check(0, 0, 0)
if cnt == 26:
    print(-1)
else:
    print(cnt)

#시작점을 찾으면 덮을 공간을 for 문으로 5 4 3 2 1 체크하고 remove하고
