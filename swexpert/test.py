def check(idx, total):
    global answer

    if idx > 11:
        if total < answer:
            answer = total
            return
    else:
        check(idx+1, total + plans[idx]*day)
        check(idx+1, total + month)
        check(idx+3, total + three_month)

for tc in range(1, int(input())+1):
    # 12달
    # 1년 이용권은 최대로 친다
    # 다 탐색
    day, month, three_month, year = map(int, input().split())
    plans = list(map(int, input().split()))
    answer = year
    check(0, 0)
    print(f'#{tc} {answer}')



'''
10      
10 40 100 300   
0 0 2 9 1 5 0 0 0 0 0 0
10 100 50 300   
0 0 0 0 0 0 0 0 6 2 7 8
'''