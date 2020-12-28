t=int(input())

def bfs(S,L):
    q=[]
    q.append(S)
    while q:
        S=q.pop()
        if dic.get(S):
            for i in dic[S]:
                if i == L:
                    return 1
                q.append(i)
    return 0


for tc in range(1,t+1):
    V,E=map(int,input().split())
    dic={}
    visited=[0]*V
    for i in range(E):
        s,e=map(int,input().split())
        if not s in dic:
            dic[s]=[e]
        else:
            dic[s].append(e)

    S,L=map(int,input().split())
    print(f'#{tc} {bfs(S,L)}')


'''
3
6 5
1 4
1 3
2 3
2 5
5 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
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