# . 평지, * 벽돌벽, # 강철벽, - 물
# ^ 위쪽을 바라보는 전차, v, < , >


command = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'S':4,
           0: '^', 1:'v', 2:'<', 3:'>',
            '^': 0, 'v':1, '<': 2, '>': 3 }
direction = ['^','v','<','>']

for tc in range(1, int(input())+1):
    H,W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    N = int(input())
    talk = list(map(str, input().rstrip()))

    for i in range(H):
        for j in range(W):
            if matrix[i][j] in direction:
                first_pos = [i, j, command[matrix[i][j]]]

    move_list=[(-1, 0), (1, 0), (0, -1), (0, 1)]
    for user in talk:
        here = command[user]
        # 포탄
        if here == 4:
            dr = first_pos[0]
            dc = first_pos[1]
            while True:
                dr += move_list[first_pos[2]][0]
                dc += move_list[first_pos[2]][1]
                if 0 > dr or dr >= H or 0> dc or dc >= W or matrix[dr][dc] == '#':
                    break
                if matrix[dr][dc] == '*':
                    matrix[dr][dc] = '.'
                    break
        # 방향을 바꾸는 명령
        else:
            r = first_pos[0]
            c = first_pos[1]
            nr = r + move_list[here][0]
            nc = c + move_list[here][1]
            matrix[r][c] = command[here]
            first_pos = [r, c, here]
            if 0 <= nr < H and 0 <= nc < W and matrix[nr][nc] == '.':
                matrix[r][c] = '.'
                matrix[nr][nc] = command[here]
                first_pos = [nr, nc, here]

    print(f'#{tc}', end =' ')
    for k in matrix:
        print(''.join(k))

