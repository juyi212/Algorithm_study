#import sys
#sys.stdin=open("input.txt","r")
#a=input()
#b=input()

T=int(input())
a = 0
for test_case in range(1,T+1):
    N = int(input())
    li = list(map(int, input().split()))
    sum=0
    for i in range(0,N-2):
        x=li[i:i+5]
        target=x[2]
        if target == max(x):
            x.sort(reverse=True)
            sum+=target-x[1]
    print(f'#{test_case} {sum}')

        #
        # if target == max(x):
        #     a=x.sort(reverse=True)
        #     print(a)

    # max_cnt = 0
    # for i in range(0, len(boxes)):
    #     target = boxes[i]
    #     cnt = 0
    #     for j in range(i + 1, len(boxes)):
    #         if boxes[j] < target:
    #             cnt += 1
    #     print(cnt)
    #     if cnt > max_cnt:
    #         max_cnt = cnt
    # print(max_cnt)
    #
    #
    #     target=x[a+2]
    #     if target==max(x):
    #         print(x.sort())

