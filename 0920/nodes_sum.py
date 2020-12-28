t=int(input())

for tc in range(1,t+1):
    N,M,L=map(int,input().split()) #노드의 개수, 리프 노드의 개수, 출력할 노드 번호
    matrix=[0]*(N+1)
    for i in range(M):
        idx,m=map(int,input().split())
        matrix[idx]=m


    while N>0:
        a=N//2
        b=(N-1)//2
        if N%2==1:
            if a==b:
                matrix[a]=matrix[N]+matrix[N-1]
                N = N - 2
        else:
            matrix[a] = matrix[N]
            N=N-1
    print(matrix[L])

'''
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962
'''