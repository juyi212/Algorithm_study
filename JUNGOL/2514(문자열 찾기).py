sentence = input()

knum = 0
inum = 0

i = 0
check = ''
while i < len(sentence):
    check += sentence[i]

    if len(check) == 3:
        if check == 'KOI':
            knum += 1
            check = ''

        elif check == 'IOI':
            inum += 1
            check = ''
        else:
            i -= 1
            check = ''
    else:
        i += 1
print(knum)
print(inum)