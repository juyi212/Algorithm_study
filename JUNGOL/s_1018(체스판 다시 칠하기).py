import sys

r, c = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

mini = []
for i in range(r-7):
    for j in range(c-7):
        cnt1, cnt2 = 0, 0
        for n in range(i, i+8):
            for m in range(j, j+8):
                if (n+m) % 2 == 0:  # 흰 검을 나눠서 count
                    if matrix[n][m] != 'W':
                        cnt1 += 1
                    if matrix[n][m] != 'B':
                        cnt2 += 1
                else:
                    if matrix[n][m] != 'B':
                        cnt1 += 1
                    if matrix[n][m] != 'W':
                        cnt2 += 1
        mini.append(cnt1)
        mini.append(cnt2)

print(min(mini))


# mini = 1000000
#
# for i in range(0, r - 7):
#     for j in range(0, c - 7):
#         f = matrix[i][j]
#         cnt = 0
#         for n in range(i, i + 8):
#             for m in range(j, j + 8):
#                 if (n + m) % 2 == 1 and matrix[n][m] == f:
#                     cnt += 1
#                 if (n + m) % 2 == 0 and matrix[n][m] != f:
#                     cnt += 1
#         if cnt > 32:
#             cnt = 64 - cnt
#         if mini > cnt:
#             mini = cnt
# print(mini)
