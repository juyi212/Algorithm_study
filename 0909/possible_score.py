import itertools

def check(idx,N,s):
    if idx==N:
        result.add(s)
        return
    check(idx+1,N,s+scores[idx])
    check(idx+1,N,s)


#모든 경우의 수를 다 봐야하는데 효율적인 방법이 뭐가있을까?
#재귀는 안됨


t=int(input())
for tc in range(1,t+1):
    N=int(input()) #문제개수
    scores=list(map(int,input().split()))
    # check(0,0)
    # print(f'#{tc} {len(result)}')
    visit=[0]*(sum(scores)+1)
    result=[0]
    for i in scores:
        for j in range(len(result)):
            if visit[result[j]+i]==0:
                result.append(result[j]+i)
                visit[result[j]+i]=1
    print(f'#{tc} {len(result)}')

'''
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1
'''
# 이런 방법도 있음.
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     num = sorted(list(map(int, input().split())))
#     m = sum(num) + 1
#     t = [0] * m
#     t[0] = 1
#
#     for i in num:
#         for j in range(m - 1, -1, -1):
#             if t[j]:
#                 t[j + i] = 1
#     print(f'#{tc}', sum(t))