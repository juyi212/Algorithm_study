two = input()

total = 0
cnt = 0
for i in range(len(two)-1, -1, -1):
    if two[i] == '1':
        total += 2 ** cnt
    cnt += 1
print(total)