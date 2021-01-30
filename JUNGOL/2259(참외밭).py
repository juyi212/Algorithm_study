n = int(input())

li = []
for _ in range(6):
    dir, sen = map(int, input().split())
    li.append(sen)

max_r = li.index(max(li))
max_c = li.index(max(li[max_r - 1], li[(max_r + 1) % 6]))

min_r = (max_r + 3) % 6
min_c = (max_c + 3) % 6

mm = li[max_r] * li[max_c]
nn = li[min_r] * li[min_c]

print(n * (mm - nn))

