import sys
sys.stdin=open("input_hw.txt","r")

def Max(a):
    li = []
    for arr in a: #행 기준 합
        sum1 = 0
        for j in range(len(arr)):
            sum1+=arr[j]
        li+=[sum1]

    for i in range(len(a)): #열 기준 합
        sum2=0
        for arr in a:
            sum2+=arr[i]
        li += [sum2]
    sum3=0
    for i in range(len(a)):
        sum3+=a[i][i]
    li += [sum3]

    sum4=0
    for i in range(len(a)):
        for j in range(len(a),-1,-1):
            if i+j ==4:
                sum4+=a[i][j]
    li += [sum4]

    return f'#{N} {max(li)}'

for test_case in range(1,11):
    N = int(input())
    a = []
    for i in range(100):
        a.append(list(map(int, input().split())))

    print(Max(a))