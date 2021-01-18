import heapq

# def solution(n, works):
#     q = []
#     for work in works:
#         heapq.heappush(q, -work)
    # heapqify(q) 오름차순
#     for i in range(n):
#         work = heapq.heappop(q)
#         if work == 0:
#             return 0
#         heapq.heappush(q, work+1)
#     answer= 0
#     for i in q:
#         answer += i**2
#     return answer

# heapq pop 은 가장 작은값을 pop 해줌
# 가장 큰것부터 pop 하기 위해서는 push 할 때 음수로 적용하여 넣어준다.

def check(n, works):
    if n >= sum(works):
        return 0
    for i in range(n):
        works[works.index(max(works))] -= 1
    answer = sum([w ** 2 for w in works])
    return answer


def heapcheck(n, works):
    p = list(map(lambda x: -x, works))
    heapq.heapify(p) # 오름차순
    # pop 할 때 가장 작은 것을 빼기 때문에
    # 음수로 바꿔서 푼다
    for _ in range(n):
        if p:
            num = heapq.heappop(p)
            if num != -1:
                heapq.heappush(p, num+1)
        else:
            break
    answer = 0
    for h in p:
        answer += h ** 2
    return answer

works = [4,3,3]
n = 4

print(heapcheck(n,works))
