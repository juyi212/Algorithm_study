# 0-9 까지 한 장씩 만
# 숫자 두 개 a, b => a+b =N

n = int(input())

ans = False

# 100000보다 작은지 큰지 확인 해야함
for i in range(1, min(100000, n)):
    # 숫자를 만들고 그냥 더 해버림
    num = str(i) + str(n-i)
    li = []
    Flag = -1
    # 중복되는 숫자가 있는지 확인 해야함
    for j in num:
        if j not in li:
            li.append(j)
        else:
            Flag = 0
            break
    if Flag:
        print(n-i, end= " ")
        print('+',end =" ")
        print(i)
        ans = True
        break
if not ans:
    print(-1)
