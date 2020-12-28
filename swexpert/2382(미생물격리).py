import sys
sys.stdin = open('input18.txt','r')

def move(m):
    if m[3] == 1:   # 상
        m[0] -= 1
        if m[0] == 0:
            m[3] = 2
            m[2] = m[2]//2
    elif m[3] == 2:  # 하
        m[0] += 1
        if m[0] == N-1:
            m[3] = 1
            m[2] = m[2] // 2
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


def check(i, j):
    c = []  # 같은 것들 끼리 모아둠
    delete = []
    for idx, a in enumerate(matrix):
        if a[0] == i and a[1] == j:
            c.append(a)
            delete.append(idx)  # 바로 없애버리면 list 이기때문에 순서가 땡겨짐
    # 따로 저장해두고 없애줘야함. 뒤에서 부터!
    new_dir = [i, j, 0, 0]
    max_v = 0
    for cc in c:
        new_dir[2] += cc[2] # 같은 것들 중 합
        if max_v < cc[2]:   # 가장 큰 것의 방향을 따라 가야함
            max_v = cc[2]
            new_dir[3] = cc[3]
    for d in range(len(delete) - 1, -1, -1):
        del matrix[delete[d]]
    matrix.append(new_dir)


def ob(k):
    if k > 0:
        p = {}  # 시간줄이기. for 문 하나라도 줄이자
        for m in matrix:
            m = move(m)
            if p.get((m[0], m[1])) is None:
                p[(m[0], m[1])] = 1
            else:
                p[(m[0], m[1])] += 1    # 충돌 되는 것이 있는지 확인
        for key, value in p.items():
            if value > 1:
                check(key[0], key[1]) # 충돌
        ob(k-1)



for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split()) # 셀의 개수, 격리시간, 미생물 군집 수
    matrix= [list(map(int, input().split())) for _ in range(K)]
    ob(M)
    result = 0
    for vv in matrix:
        result += vv[2]
    print(f'#{tc} {result}')

    # 부딪히면 직전으로 돌아감 -> 약있는 부분임
    # 1 상, 2 하 , 좌 3, 우 4
