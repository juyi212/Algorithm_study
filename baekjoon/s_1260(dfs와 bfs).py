# dfs 와 bfs 문제

def dfs(v):
    visited.append(v)

    for i in range(N+1):
        if tree[v][i] != 0 and i not in visited:
            dfs(i)


def bfs(v):
    q = []
    q.append(v)
    visited.append(v)
    while q:
        n = q.pop(0)
        for i in range(N+1):
            if tree[n][i] == 1 and i not in visited:
                q.append(i)
                visited.append(i)



N, M, V = map(int, input().split())
tree = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    s, e = map(int, input().split())
    tree[s][e] = 1
    tree[e][s] = 1

visited=[]
dfs(V)
print(*visited)
visited=[]
bfs(V)
print(*visited)
