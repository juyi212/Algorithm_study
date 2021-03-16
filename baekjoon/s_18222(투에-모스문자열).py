k = int(input())

# 맨 처음에 0으로 시작
if k != 1:
    new = format(k, 'b')
    a = new.count('1')
    print(a % 2)
else:
    print(0)
