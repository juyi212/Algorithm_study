def check(idx, taste, total):
    global max_taste
    if total > L:
        return
    if max_taste < taste:
        max_taste = taste

    if idx == N:    # 순서도 중요하나..?ㅇㅅㅇ
        return

    f, k = diet[idx]
    check(idx+1,taste+f, total+k)
    check(idx+1,taste, total)


for tc in range(1, int(input())+1):
    N, L = map(int, input().split()) # 개수, 제한된 칼로리
    diet = []
    for i in range(N):
        T, K = map(int, input().split()) # 맛, 칼로리
        diet.append([T, K])
    max_taste = 0
    check(0, 0, 0)
    print(f'#{tc} {max_taste}')


'''
1
5 1000
100 200
300 500
250 300
500 1000
400 400
'''