import sys
sys.stdin = open('input15.txt','r')


def check(n, m, honey, total, cnt):
    global max_h, now

    if total > C:   # 제한된 양을 넘어섰을 때
        return

    if cnt == M: # 재취한 벌통개수가 M 일 때
        if honey > max_h:
            max_h = honey
            return

    if m >= N: # index 넘어가면 pass
        return

    check(n, m+1, honey+(honey_boxes[n][m]**2), total+honey_boxes[n][m], cnt+1)
    check(n, m + 1, honey, total, cnt+1)    # 벌꿀채취는 함 , 그 중에서 C를 안넘는것을 선별


for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split()) # 벌통들의 크기, 벌통의 개수, 꿀 채취 최대 양
    honey_boxes = [list(map(int, input().split())) for _ in range(N)]
    # 같은행에서 선택 못하게 하자 (댓글 참조) - 이렇게 풀면 x
    answer = [0 for _ in range(N)]
    for i in range(N): # 각각의 일꾼들 한 행씩 차지
        for j in range(N-M+1):  # 벌통 index
            max_h = -1
            check(i, j, 0, 0, 0)
            answer[i] = max(answer[i], max_h)

    answer.sort()
    print(f'#{tc} {answer[N-1]+answer[N-2]}')



'''

1
3 3 10
7 2 9
6 6 6
5 5 7

'''