t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    flag=[input() for _ in range(n)]
    w=[0]*n
    b=[0]*n
    r=[0]*n
    for i in range(n):
        for j in range(m):
            if flag[i][j] !='W':
                w[i]+=1
            if flag[i][j] !='B':
                b[i]+=1
            if flag[i][j] !='R':
                r[i]+=1
    for i in range(n-1):
        w[i+1]+=w[i]
        b[i + 1] += b[i]
        r[i + 1] += r[i]
    min_v=n*m
    for i in range(n-2): # 범위 설정 w 경우로 생각해보기
        for j in range(i+1,n-1): # b 경우으로 생각해보기
            s1=w[i]
            s2=b[j]-b[i] #중간 범위
            s3=r[n-1]-r[j]  # i가 될 수 없는 이유는 적어도 한칸은 w
            if min_v>s1+s2+s3:
                min_v=s1+s2+s3
    print(f'#{tc} {min_v}')

'''
1
4 5
WRWRW
BWRWB
WRWRW
RWBWR

'''


# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     flag = [input() for _ in range(N)]
#
#     W = [0] * N
#     B = [0] * N
#     R = [0] * N
#     for i in range(N):
#         for j in range(M):
#             if flag[i][j] != 'W':
#                 W[i] += 1
#             if flag[i][j] != 'B':
#                 B[i] += 1
#             if flag[i][j] != 'R':
#                 R[i] += 1
#
#     for i in range(1, N):
#         W[i] += W[i - 1]
#         B[i] += B[i - 1]
#         R[i] += R[i - 1]
#     minV = N * M
#     for i in range(N - 2):
#         for j in range(i + 1, N - 1):
#             s1 = W[i]
#             s2 = B[j] - B[i]
#             s3 = R[N - 1] - R[j]
#             if minV > s1 + s2 + s3:
#                 minV = s1 + s2 + s3
#     print(f'#{tc} {minV}')