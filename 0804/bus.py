import sys
sys.stdin=open('sample_input_bus.txt','r')

T=int(input())
for test_case in range(1,T+1):
    K, N, M = map(int, input().split())
    li = list(map(int, input().split()))
    m = 0
    st = 0
    st += K
    for j in range(0,M-1):
        if li[j+1]-li[j]>K:
            m = 0
            print(f'#{test_case} {m}')
            break
    for i in range(N):
        for q in range(N):
            if st in li:
                if st >= N:
                    break
                m += 1
                st+=K
                continue
            else:
                if st >= N:
                    break
                st -= 1

    if st >= N:
        print(f'#{test_case} {m}')

# n = int(input())
#
# li = []
#
# for i in range(n):
#     K, N, M = map(int, input().split())
#     li = list(map(int, input().split()))
#     where = 0
#     cnt = 0
#     for k in range(1,len(li)):
#         if li[k]-li[k-1] > K:
#             where = N
#     while(where < N):
#         where += K
#         if where >= N:
#             break
#         while(where not in li):
#             where -= 1
#         cnt += 1
#
#     print(f'#{i+1} {cnt}')