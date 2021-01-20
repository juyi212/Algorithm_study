import sys
from heapq import heappush, heappop


def check(matrix, min_time):
    q = [(0, 1)]
    while q:
        time, s = heappop(q)

        if min_time[s] != time:
            # heap 안에 각 노드마다의 최소값이 있을 수 있다.
            # min_time 과 다르면 continue로 넘어가자
            continue

        for e, l, t in matrix[s]:
            # 퇴근시간보다 넘어섰을 때 또는 퇴근시간과 겹치지 않을 때

            if time >= E or not t:
                if min_time[e] > time + l:
                    min_time[e] = time + l
                    heappush(q, (time+l, e))
            # 겹칠 때
            else:
                t_copy = time
                # 퇴근시간 전
                if t_copy < S:
                    # 더해질 값이 막히는시간을 넘어가느냐 안넘어가느냐
                    del_time = min(S-t_copy, l)
                    t_copy += del_time
                    l -= del_time # 안넘어가면 0, 넘어가면 부분이 남음

                if S <= t_copy < E:
                    del_time = min(E-t_copy, l*2)   # 시간은 두 배
                    t_copy += del_time
                    l -= del_time/2 # 거리는 1/2

                if t_copy >= E: # 윗부분에서 더해주다가 E가 넘고, l이 남아 있을 때 더 해준다.
                    t_copy += l

                if min_time[e] > t_copy: # 최소값을 찾아준다.
                    min_time[e] = t_copy
                    heappush(q, (t_copy, e))


N, M, S, E = map(int, sys.stdin.readline().split())
# N개 지점, M 간선, S, E 퇴근 시작 끝
INF = float('inf')
matrix= [[] for _ in range(N+1)]

for i in range(M):
    A, B, L, t1, t2 = map(int, sys.stdin.readline().split())
    # t1 A->B 막힘
    # t2 B->A 막힘
    matrix[A].append([B, L, t1])
    matrix[B].append([A, L, t2])

min_time =[INF for _ in range(N+1)]
min_time[1] = 0
check(matrix, min_time)

a = 0
for i in range(1, N+1):
    if min_time[i] != INF and min_time[i] > a:
        a = min_time[i]

if int(a) == a:
    print(int(a))
else:
    print(a)

# 최소비용까지 구함
# 이어지는 구간
# 이어지지않는 구간
# 다익스트라는 무조건 heap!!!!!

