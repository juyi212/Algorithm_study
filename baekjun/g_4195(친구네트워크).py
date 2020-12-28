# 승한스 풀이 : disjoint set의 크기를 구하면 된다


# 분리집합 문제
import sys


def find(x):
    if parents[x] == x: # 가장 최상단의 부모 노드를 찾아서 리턴
        return x

    p = find(parents[x])
    parents[x] = p  # 부모를 갱신해줌 트리를 압축
    return p


def union(person1, person2, cnt):
    a = find(person1)
    b = find(person2)

    if a != b:
        parents[b] = a
        cnt[a] += cnt[b]


for tc in range(1, int(sys.stdin.readline())+1):
    n = int(sys.stdin.readline())
    parents = {}
    cnt = {}
    for i in range(n):
        p1, p2 = sys.stdin.readline().split()
        if p1 not in parents:   # 각각을 집합처럼 저장
            parents[p1] = p1
            cnt[p1] = 1
        if p2 not in parents:
            parents[p2] = p2
            cnt[p2] = 1
        union(p1, p2, cnt)  # 부모 노드를 찾아서 이름과 cnt를 저장해준다.
        print(cnt[find(p1)])


# import sys
# T = int(input())
# for tc in range(T):
#     F = int(input())
#     set_li = []
#     for i in range(F):
#         a, b = sys.stdin.readline().split()
#         tmp = []
#         cnt = 0
#         result = 2
#         for j in range(len(set_li)):
#             if a in set_li[j] or b in set_li[j]:
#                 set_li[j].add(a)
#                 set_li[j].add(b)
#                 tmp.append(j)
#                 cnt += 1
#                 result = len(set_li[j])
#                 if len(tmp) == 2:
#                     set_li[tmp[0]] = set_li[tmp[0]] | set_li[tmp[1]]
#                     del set_li[tmp[1]]
#                     result = len(set_li[tmp[0]])
#                     break
#         else:
#             if not cnt:
#                 set_li.append({a, b})
#         print(result)