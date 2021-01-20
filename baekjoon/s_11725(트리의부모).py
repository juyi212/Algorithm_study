import sys
N = int(input())
nodes = [[] for _ in range(N+1)]
for i in range(N-1):
    s, e = map(int, sys.stdin.readline().split())
    nodes[s].append(e)
    nodes[e].append(s)

q = list()
head = [0]*(N+1)
q.append(1)
print(nodes)
while q:
    v = q.pop(0)
    for node in nodes[v]:
        if not head[node]:  #자식 idx 부모 v
            head[node] = v
            q.append(node)
print(head)
for j in range(2, N+1):
    print(head[j])