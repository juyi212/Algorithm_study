 def find_set(x):
    if x == parent[x]:
        return x

    p = find_set(parent[x])
    parent[x] = p
    return p


def union(x, y):
    a = find_set(x)
    b = find_set(y)
    if a != b:
        parent[b] = a



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())    # N 명, M 쪽지 횟수
    parent = list(range(N+1))
    p = list(map(int, input().split()))
    for i in range(M):
        p1, p2 = p[i*2], p[i*2+1]
        union(p1, p2)   # 합치기

    result = []
    for i in range(N+1):
        result.append(find_set(parent[i]))  # 갱신
        # 5,6 에서 4의 대표인 7으로 다 바뀐다.
    new = set(result)
    print('#{} {}'.format(tc, len(new)-1))


# 교수님 풀이
# def bfs(st):
#     queue = [st]
#     team[st] =  True
#
#     while len(queue) > 0:
#         curr =  queue.pop(0)
#
#         for i in range(1, V+1):
#             if not team[i] and adj[curr][i]:
#                 team[i] = True
#                 queue.append(i)
#
#
#
# team = [False] * (V+1)
#
# and = 0
# for i in range(1, V+1):
#     if not team[i]:
#         ans += 1
#         bfs(i)








'''
1
7 4
2 3 4 5 4 6 7 4
'''
'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4

'''