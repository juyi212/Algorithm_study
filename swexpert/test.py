direction = {
    1: (-1, 0), 2: (1, 0),
    3: (0, -1), 4: (0, 1)
}

def move(m):
    if m[3] == 1:   # 상
        m[0] -= 1
        if m[0] == 0:
            m[2] = m[2]//2
            m[3] = 2
    elif m[3] == 2: #하
        m[0] += 1
        if m[0] == N-1:
            m[2] = m[2]//2
            m[3] = 1
    elif m[3] == 3:  # 좌
        m[1] -= 1
        if m[1] == 0:
            m[3] = 4
            m[2] = m[2] // 2
    elif m[3] == 4:  # 우
        m[1] += 1
        if m[1] == N-1:
            m[3] = 3
            m[2] = m[2] // 2

    return m

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split()) # 셀의 개수, 격리시간, 미생물 군집 수
    matrix = dict()
    for _ in range(K):
        r, c, bug, dir = map(int, input().split())
        matrix[(r, c)] = [(bug, dir)]
    # dict 으로 풀어도 가능/ dict 으로 풀면 del 과정을 없애도 됨
    for p in range(M):
        check = {}
        for key, value in matrix.items():
            cr, cc = key
            bug, di = value[0][0], value[0][1]
            m = move([cr,cc,bug,di])
            # 충돌되는 것 확인해야함
            if (m[0], m[1]) in check:
                check[(m[0], m[1])].append((m[2], m[3]))
            else:
                check[(m[0], m[1])] = [(m[2], m[3])]

        for i in check:
            if len(check[i]) > 1:
                total = 0
                next_dir = (0, 0)
                find_max = 0
                for bugs, currentdir in check[i]:
                    total += bugs
                    if bugs > find_max:
                        find_max = bugs
                        next_dir = currentdir
                check[i] =[(total, next_dir)]
        matrix = check

    result = 0
    for vv in matrix:
        result += matrix[vv][0][0]
    print(f'#{tc} {result}')






































