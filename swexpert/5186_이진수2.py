for tc in range(1, int(input())+1):
    num = float(input())
    y = '0.'
    t = True

    while True:
        if len(y) > 15:
            t = False
            break
        if num == 1:
            break
        a = float(num) * 2

        if a > 1:   # 맨 앞의 1을  y 에 넣어주고
            s = str(a)
            y += s[0]
            new = '0.'  # 소수점 부분을 가져오기 위해 슬라이싱 해준다.
            new += s[2::]
            num = new
        else:   # 1을 넘지 않을 때
            s = str(a)
            y += s[0]   # 정수부분 0을 넣어줌
            num = a

    if t:
        print('#{0} {1}'.format(tc, y[2::]))
    else:
        print('#{0} {1}'.format(tc, 'overflow'))
'''
3
0.625
0.1
0.125
'''
'''
1
0.1
'''