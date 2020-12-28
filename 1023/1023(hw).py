string = input()

for i in range(0, len(string), 7):
    new = []
    for j in range(i, i+7):
        new += string[j]

    new = new[::-1]
    total = 0
    for i in range(len(new)):
        if new[i] == '1':
            total += 2**int(i)

    print(total, end=' ')

'''
0000000111100000011000000111100110000110000111100111100111111001100111
'''