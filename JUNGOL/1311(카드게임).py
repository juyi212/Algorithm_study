def check():
    # 1번째
    rules[0] = True
    for i in range(1, 5):
        if color[0] != color[i]:
            rules[0] = False
            break

    m = number[0]
    for i in range(1, 5):
        if number[i] != m + i:
            rules[0] = False
            break

    if rules[0]:
        return 900 + max(number)

    # 2번째

    if number[0] == number[3] or number[1] == number[4]:
        rules[1] = True

    if rules[1]:
        return 800 + number[2]

    # 3번째
    if number[0] == number[2] and number[3] == number[4]:
        th = number[0]
        tw = number[3]
        rules[2] = True

    elif  number[0] == number[1] and number[2] == number[4]:
        th = number[2]
        tw = number[0]
        rules[2] = True

    if rules[2]:
        return th*10 + tw + 700

    # 4번째

    if color[0] == color[4]:
        rules[3] = True

    if rules[3]:
        return max(number) + 600

    # 5번째
    m = number[0]
    rules[4] = True
    for i in range(1, 5):
        if number[i] != m + i:
            rules[4] = False

    if rules[4]:
        return max(number) + 500

    # 6번째

    if number[0] == number[2] or number[1] == number[3] or number[2] == number[4]:
        rules[5] = True
    if rules[5]:
        return number[2] + 400

    # 7번쨰
    if number[0] == number[1] and number[2] == number[3]:
        rules[6] = True
    if number[0] == number[1] and number[3] == number[4]:
        rules[6] = True
    if number[2] == number[1] and number[3] == number[4]:
        rules[6] = True

    if rules[6]:
        return number[3] * 10 + number[1] + 300

    # 8번째
    if number[0] == number[1]:
        num = number[0]
        rules[7] = True
    if number[1] == number[2]:
        num = number[1]
        rules[7] = True
    if number[2] == number[3]:
        num = number[2]
        rules[7] = True
    if number[3] == number[4]:
        num = number[3]
        rules[7] = True

    if rules[7]:
        return num + 200

    if True not in rules:
        return 100 + max(number)






color, number = [], []
rules = [False] * 8
for _ in range(5):
    c, n = input().split()
    color.append(c)
    number.append(int(n))

color.sort()
number.sort()
print(check())



