matrix = [list(input().rstrip()) for _ in range(5)]

max_l = -1
for i in matrix:
    if len(i) > max_l:
        max_l = len(i)

for i in range(max_l):
    for j in range(5):
        if len(matrix[j]) < max_l:
            matrix[j].append('')
            continue

total = ''
for i in range(max_l):
    for j in range(5):
        total += matrix[j][i]
print(total)