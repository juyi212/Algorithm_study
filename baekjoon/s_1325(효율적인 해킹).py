import sys
from collections import deque


# pypy 제출

def bfs(v):
    q = deque()
    q.append(v)
    visited = [False] * (n + 1)
    visited[i] = True
    cnt = 1
    while q:
        v = q.popleft()
        for num in matrix[v]:
            if not visited[num]:
                cnt += 1
                visited[num] = True
                q.append(num)
    return cnt


n, m = map(int, sys.stdin.readline().split())
matrix = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    matrix[e].append(s)

ans = []
max_v = -1
for i in range(1, n + 1):
    if matrix[i]:
        t = bfs(i)
        if max_v == t:  # 같을 때는 그 노드 번호 오름차순으로 다 출력해야 함
            ans.append(i)
        if max_v < t:  # 큰 것
            max_v = t
            ans = []
            ans.append(i)

print(*ans)




