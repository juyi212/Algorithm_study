def check(short_arr,long_arr):
    global max_v
    i=0
    j=0
    sum_v=0
    k=0
    while True:
        sum_v+=long_arr[j]*short_arr[i]
        i+=1
        j+=1
        if i==len(short_arr):
            if sum_v>=max_v:
                max_v=sum_v
            k+=1
            i=0
            j=k
            sum_v=0
        elif j==len(long_arr):
            break
    return f'#{tc} {max_v}'


t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    max_v=0
    if len(a)<len(b):
        print(check(a,b))
    else:
        print(check(b,a))