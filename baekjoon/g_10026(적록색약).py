import sys
from collections import deque


def bfs(ch, r, c, what):
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        if r - 1 > -1 and (what == ch[r-1][c]):
            q.append((r-1, c))
            ch[r-1][c] = 0
        if r + 1 < n and (what == ch[r+1][c]):
            q.append((r+1, c))
            ch[r+1][c] = 0
        if c - 1 > -1 and (what == ch[r][c-1]):
            q.append((r, c-1))
            ch[r][c-1] = 0
        if c + 1 < n and (what == ch[r][c+1]):
            q.append((r, c+1))
            ch[r][c+1] = 0

# 구역
# 적록색약이 아닌 사람과 적록색약인 사람이 그림을 봤을 때의 구역 수를 구하기
# bfs
# 2*N^2 -> 1초... 충분하겠고만

n = int(input())
drawing = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
blind = [[0] * n for _ in range(n)]
# 적록색약 배열
for i in range(n):
    for j in range(n):
        if drawing[i][j] == 'R' or drawing[i][j] == 'G':
            blind[i][j] = 1
        else:
            blind[i][j] = 2

not_blind = 0
y_blind = 0
for i in range(n):
    for j in range(n):
        if drawing[i][j] != 0:
            not_blind += 1
            bfs(drawing, i, j, drawing[i][j])
        if blind[i][j] != 0:
            y_blind += 1
            bfs(blind, i, j, blind[i][j])
print(not_blind, end=' ')
print(y_blind)


'''
5
BBBBB
BBGBG
BGGGG
BBRRR
RRRRR
'''
