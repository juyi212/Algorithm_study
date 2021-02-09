import sys

# 시간 엄청...걸림
# 일단 두팀으로 나눠지는 경우의 수를 다 구한다음
# 한 번 구해지는 즉시 바로 start, link 를 나눠서 계산
# min_v 까지

def check(idx):
    global min_v

    if idx >= n:
        return
    if checkit.count(1) == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if checkit[i] and checkit[j]:
                    # 돌면서 1,3 3,1 다 더 함 ~~~
                    start += teams[i][j]
                elif not checkit[i] and not checkit[j]:
                    link += teams[i][j]
        min_v = min(min_v, abs(start-link))
        # start = []
        # link = []
        # for i in range(len(checkit)):
        #     if checkit[i] == 1:
        #         start.append(i)
        #     else:
        #         link.append(i)
        # cnt1 = 0
        # for i in range(len(start)):
        #     for j in range(i, len(start)):
        #         cnt1 += teams[start[i]][start[j]]
        #         cnt1 += teams[start[j]][start[i]]
        #
        # cnt2 = 0
        # for i in range(len(link)):
        #     for j in range(i, len(link)):
        #         cnt2 += teams[link[i]][link[j]]
        #         cnt2 += teams[link[j]][link[i]]
        #
        # if min_v > abs(cnt1- cnt2):
        #     min_v = abs(cnt1-cnt2)

    checkit[idx] = 1
    check(idx+1)
    checkit[idx] = 0
    check(idx+1)

n = int(sys.stdin.readline())
teams = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 팀은 n//2 로 두팀으로 나누어짐
# 스타트팀, 링크팀
result = []
checkit = [0] * n
min_v = 1e9
check(0)
print(min_v)





   
# another method
# def sol(start, link, s1, s2, i):
#     # 스타트와 링크를 동시에 처리
#     if i == n:
#         ret.append(abs(s1-s2))
#         return
#
#     # 하나씩 채워가며 뺴고 ~~
#     if len(start) < n//2:
#         start.append(i)
#         temp = 0
#         for j in start:
#             temp += teams[j][i] + teams[i][j]
#         sol(start, link, s1+temp, s2, i+1)
#         start.pop()
#
#     if len(link) < n//2:
#         link.append(i)
#         temp = 0
#         for j in link:
#             temp += teams[j][i] + teams[i][j]
#         sol(start, link, s1, s2+temp, i+1)
#         link.pop()
#     return
#
#
# n = int(sys.stdin.readline())
# teams = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# ret = []
# sol([0], [], 0, 0, 1)
