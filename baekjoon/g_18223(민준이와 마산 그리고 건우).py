# 다익스트라
# 최단 경로
# 최단 경로에 건우가 있는 곳이 포함되면 save item 아니면 good bye
import sys
from collections import deque


def bfs():
    visited[1] = 0
    q = deque()
    if p == 1:
        q.append([1, 0, True])
    else:
        q.append([1, 0, False])
    while q:
        node, total, gen = q.popleft()
        if node == v:
            if gen:
                return 'SAVE ITEM'
        for num in matrix[node]:
            new, tmp = num[0], num[1]
            if visited[new] >= tmp + total:
                visited[new] = tmp + total
                if new == p:
                    q.append([new, tmp + total, True])
                else:
                    q.append([new, tmp + total, gen])
    return 'GOOD BYE'


v, e, p = map(int, sys.stdin.readline().split())  # 정점, 간선, 건우 위치
INF = float('inf')
visited = [INF] * (v + 1)
matrix = [[] for _ in range(v + 1)]
for i in range(e):
    s, e, w = map(int, sys.stdin.readline().split())
    matrix[s].append([e, w])
    matrix[e].append([s, w])

print(bfs())
