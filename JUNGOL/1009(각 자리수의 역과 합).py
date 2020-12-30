while 1:
    nn = int(input())
    if nn == 0:
        break
    else:
        total = 0
        r_num = nn
        r_num = str(r_num)
        r_num = list(r_num.rstrip())
        r_num = r_num[::-1]
        n_num = ''.join(r_num)
        n_num = n_num.lstrip('0')
        print(n_num, end =' ')

        while True:
            total += nn % 10
            nn = nn//10
            if nn == 0:
                break
        print(total)

        # while True:
        #     num = (num*10) + (nn % 10) # 반대로 reverse 하는거
        #     total += nn%10
        #     nn = nn//10
        #     if nn == 0:
        #         break

