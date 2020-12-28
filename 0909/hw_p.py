def in_order(n):
    if len(heap[n]) >= 2: #왼쪽
        in_order(int(heap[n][1]) - 1)
    print(heap[n][0], end='')
    if len(heap[n]) >= 3: #오른쪽도 존재한다는 것임
        in_order(int(heap[n][2]) - 1)


T = 10
for tc in range(1, T + 1):
    N = int(input())
    in_li = [input().split() for _ in range(N)]
    heap = [n[1:] for n in in_li]
    print(f'#{tc} ', end='')
    in_order(0)
    print()