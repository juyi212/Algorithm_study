t=int(input())
for tc in range(1,t+1):
    N,M,L=map(int,input().split()) #노드의 개수, 리프 노드의 수 , 값을 출력할 노브 번호
    tree=[0]*(N+1)
    for i in range(M):
        idx,num=map(int,input().split())
        tree[idx]=num

    if N%2==1: #홀
        for i in range(N,1,-2):
            tree[i//2]=tree[i]+tree[i-1]
    else:
        tree[N//2]=tree[N]
        for i in range(N-1,1,-2):
            tree[i // 2] = tree[i] + tree[i - 1]
    print(f'#{tc} {tree[L]}')


    # for i in range(N-M,0,-1): 교수님
    #
    # 님
    # [i]=T[i*2]
    # if i *2 +1 <=N:
    #     T[i]+=T[i*2+1]

'''
1
5 3 2
4 1
5 2
3 3
'''