t=int(input())

def maketree(n):
    global cnt
    if n<=N:
        maketree(n*2)
        cnt+=1
        arr[n]=cnt
        maketree((n*2)+1)


for tc in range(1,t+1):
    N=int(input())
    arr=[0]*(N+1)
    cnt=0
    maketree(1)
    print(arr[1],arr[N//2])
    print(arr)