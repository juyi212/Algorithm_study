# 시작지점으로 3방향

def check(r, c, a):

    for dr, dc in [(0, 1),(1, 1),(-1, 1),(1,0)]:
        nr, nc = r+dr, c + dc
        if 0 <= nr < 19 and 0 <= nc < 19:
            if matrix[nr][nc] == a:
                cnt = 2
                while True:
                    nr += dr
                    nc += dc
                    if 0 <= nr < 19 and 0 <= nc < 19:
                        if matrix[nr][nc] == a:
                            cnt += 1
                        if matrix[nr][nc] != a:
                            break
                    else:
                        break

                if cnt == 5: # 전의 값도 살펴주기
                    nr = r - dr
                    nc = c - dc
                    if 0 > nr or nr > 19 or 0 > nc or nc > 19 or matrix[nr][nc] != a:
                        return cnt



matrix = [list(map(int, input().split())) for _ in range(19)]

ch = False
for i in range(19):
    for j in range(19):
        if matrix[i][j] == 1 or matrix[i][j] == 2:
            ans = check(i,j, matrix[i][j])
            if ans == 5:
                ch = True
                print(matrix[i][j])
                print(i+1, j+1)
                break
if not ch:
    print(0)