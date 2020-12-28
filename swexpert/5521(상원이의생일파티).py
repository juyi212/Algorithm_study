def bfs(v):
    queue = []
    queue.append([v, 0])
    while queue:
        v, cnt = queue.pop(0)
        if cnt == 3:
            return

        if v not in visited:
            visited.append(v)

        for w in friends[v]:
            if w not in visited:
                queue.append([w, cnt+1])


for tc in range(1, int(input())+1):
    n, m = map(int, input().split()) # n명, m 간선수

    friends = [[] for _ in range(n+1)]
    for i in range(m):
        s, e = map(int, input().split())
        friends[s].append(e)
        friends[e].append(s)
    visited = []
    bfs(1)
    print('#{} {}'.format(tc, len(visited)-1))


'''
1
6 5
1 2
1 3
3 4
2 3
4 5


'''