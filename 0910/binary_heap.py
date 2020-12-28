
import heapq

t = int(input())
for tc in range(1,t+1):
    N = int(input())
    heapp = list(map(int,input().split()))
    heap = []
    #라이브러리는 하나씩이 아니라 들어와져있는 값들을 최소힙으로 만들기때문에
    #약간의 차이가 있을 수 있다.
    # 들어온 값들을 하나씩 최소힙으로 정렬시켜주자.

    for i in range(N):
        heapq.heappush(heap, heapp[i])
    heap.insert(0, 0)

    a = N
    f = 0
    print(f'#{tc}',end=' ')
    while True:
        if a < 1:
            break
        a = a//2
        f += heap[a]
    print(f)

'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''