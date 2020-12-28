

def bfs(node):
    q=[]
    q.append(node)
    while q:
        s=q.pop(0)
        for w in range(1,com+1):
            if matrix[s][w]==1 and not w in visit:
                q.append(w)
                visit.append(w)
    return

com=int(input()) #컴퓨터 대수
n=int(input()) #쌍의 수
matrix=[[0]*(com+1) for _ in range(com+1)]
visit=[]
for i in range(n):
    s,e=map(int,input().split())
    matrix[s][e]=1
    matrix[e][s]=1
bfs(1)
print(len(visit)-1)



'''
2 1

2 1

답은 1입니다.
'''