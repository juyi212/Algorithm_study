from copy import deepcopy


def check(array):
    #   해당 면에서 바뀌는
    array[0][0], array[2][0], array[2][2], array[0][2] = array[2][0], array[2][2], array[0][2], array[0][0]
    array[0][1], array[1][0], array[2][1], array[1][2] = array[1][0], array[2][1], array[1][2], array[0][1]


def U(d):
    if d == '+':
        k = 1
    elif d == '-':
        k = 3
    for _ in range(k):
        check(cube[0])
        a = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
        cube[4][0][0], cube[4][0][1], cube[4][0][2] = cube[5][0][0], cube[5][0][1], cube[5][0][2]
        cube[5][0][0], cube[5][0][1], cube[5][0][2] = cube[3][0][0], cube[3][0][1], cube[3][0][2]
        cube[3][0][0], cube[3][0][1], cube[3][0][2] = a


def F(d):
    if d == '+':
        k = 1
    elif d == '-':
        k = 3
    for _ in range(k):
        check(cube[1])
        a = cube[0][2][0], cube[0][2][1], cube[0][2][2]
        cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
        cube[3][2][2], cube[3][1][2], cube[3][0][2] = cube[2][2][0], cube[2][2][1], cube[2][2][2]
        cube[2][2][0], cube[2][2][1], cube[2][2][2] = cube[4][0][0], cube[4][1][0], cube[4][2][0]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = a


def D(d):
    if d == '+':
        k = 1
    elif d == '-':
        k = 3
    for _ in range(k):
        check(cube[2])
        a = cube[1][2][0], cube[1][2][1], cube[1][2][2]
        cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]
        cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[5][2][0], cube[5][2][1], cube[5][2][2]
        cube[5][2][0], cube[5][2][1], cube[5][2][2] = cube[4][2][0], cube[4][2][1], cube[4][2][2]
        cube[4][2][0], cube[4][2][1], cube[4][2][2] = a


def L(d):
    if d == '+':
        k = 1
    elif d == '-':
        k = 3
    for _ in range(k):
        check(cube[3])
        a = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        cube[5][2][2], cube[5][1][2], cube[5][0][2] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
        cube[2][2][2], cube[2][1][2], cube[2][0][2] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = a


def R(d):
    if d == '+':
        k = 1
    elif d == '-':
        k = 3
    for _ in range(k):
        check(cube[4])
        a = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[2][2][0], cube[2][1][0], cube[2][0][0]
        cube[2][2][0], cube[2][1][0], cube[2][0][0] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        cube[5][2][0], cube[5][1][0], cube[5][0][0] = a


def B(d):
    if d == '+':
        k = 1
    elif d == '-':
        k = 3
    for _ in range(k):
        check(cube[5])
        a = cube[0][0][0], cube[0][0][1], cube[0][0][2]
        cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[4][0][2], cube[4][1][2], cube[4][2][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[2][0][0], cube[2][0][1], cube[2][0][2]
        cube[2][0][0], cube[2][0][1], cube[2][0][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = a


CUBE = [[[] for _ in range(3)] for _ in range(6)]

# 큐브 초기화
s = 'wrygbo'  # U F D L R B
for i in range(6):
    for j in range(3):
        for _ in range(3):
            CUBE[i][j].append(s[i])


t = int(input())
for _ in range(t):
    n = int(input())
    cmd = input().split()
    cube = deepcopy(CUBE)
    while cmd:
        c = cmd.pop(0)
        if c[0] == 'U':
            U(c[1])
        elif c[0] == 'F':
            F(c[1])
        elif c[0] == 'D':
            D(c[1])
        elif c[0] == 'L':
            L(c[1])
        elif c[0] == 'R':
            R(c[1])
        elif c[0] == 'B':
            B(c[1])

        # cnt=-1
        # for i in cube:
        #     cnt += 1
        #     print(cnt, i)
        # print("------------------------------------")
    for i in range(3):
        hi = ''.join(cube[0][i])
        print(hi)


'''
1
16
B+ D- U+ F- R- B+ B- B- R- R- U+ L- L+ L- R+ B-

yrg
bwg
bbg

'''
'''
1
4
B+ D- U+ F-


'''
'''
1
8
U+ B- R- F- D+ L- B+ U-

정답
rgo
bwo
wby
'''

'''
1
16
U+ R+ R+ F+ F+ R+ R+ U+ F+ F+ R+ R+ F+ F+ U- L+

정답
oyw
oww
byw

'''