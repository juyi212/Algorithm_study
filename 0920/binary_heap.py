import heapq

t=int(input())
for tc in range(1,t+1):
    N=int(input())
    heapp=list(map(int,input().split()))
    heap=[]
    for i in range(N):
        heapq.heappush(heap,heapp[i])
    print(heap)

    heap.insert(0,0)
    sum_p=0
    end=N

    while end!=1:
        pp=end//2
        sum_p+=heap[pp]
        end=pp
    print(f'#{tc} {sum_p}')

# import heapq
#
# t = int(input())
# for tc in range(1,t+1):
#     N = int(input())
#     heapp = list(map(int,input().split()))
#     heap = []
#     #라이브러리는 하나씩이 아니라 들어와져있는 값들을 최소힙으로 만들기때문에
#     #약간의 차이가 있을 수 있다.
#     # 들어온 값들을 하나씩 최소힙으로 정렬시켜주자.
#
#     for i in range(N):
#         heapq.heappush(heap, heapp[i])
#     heap.insert(0, 0)
#
#     a = N
#     f = 0
#     print(f'#{tc}',end=' ')
#     while True:
#         if a < 1:
#             break
#         a = a//2
#         f += heap[a]
#     print(f)