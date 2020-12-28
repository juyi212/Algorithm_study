import collections
def bfs():
    white=['0']*9
    q=collections.deque()
    q.append((white,0))
    while q: #극히 드문 케이스가 있을것이야....
        white,cnt=q.popleft()
        if white == target:
            return cnt
        for i in value:
            n_white=list(white[:])
            for j in i:
                if n_white[j]=='0':
                    n_white[j]='1'
                else:
                    n_white[j]='0'
            new=''.join(n_white)
            if not new in visit:
                visit.add(new)
                q.append((new,cnt+1))
    return

t=int(input())
for tc in range(t):
    matrix=[list(input()) for _ in range(3)] # 흰보드를 이렇게 만들어야함.
    target=''
    for i in range(3):
        for j in range(3):
            if matrix[i][j]=='*':
                target+='1'
            else:
                target+='0'
    value=[{0,1,3},{1,0,2,4},{2,1,5},{3,0,4,6},{4,1,5,7,3},{5,2,4,8},{6,3,7},{7,4,8,6},{8,5,7}]#바꿨을 때 뒤집히는 것들
    visit=set()
    print(bfs())



'''
2
*..
**.
*..
***
***
***
'''