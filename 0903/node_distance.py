def check(n):
    q=[]
    q.append((n,0))
    visited[n]=1
    while q:
        node,length=q.pop(0)
        for w in range(V+1):
            if matrix[node][w]==1 and visited[w]==0:
                if w==end:
                    return length+1
                    break
                q.append((w,length+1))
                visited[w]=1
    return 0
t=int(input())
for tc in range(1,t+1):
    V,E =map(int,input().split())
    matrix=[[0]*(V+1) for _ in range(V+1)]
    visited=[0]*(V+1)
    for i in range(E):
        s,e=map(int,input().split())
        matrix[s][e]=1 #양방향임
        matrix[e][s]=1
    start,end=map(int,input().split())
    print(f'#{tc} {check(start)}')

'''

3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''