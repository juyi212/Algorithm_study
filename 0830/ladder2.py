import sys
sys.stdin=open("ladder_input.txt","r")

def ladder_check():
    global count
    result=[100000]*100
    dr=[1,0,0]
    dc=[0,1,-1]
    for i in range(100):
        if ladder[0][i]==1:
            visited=[[0]*100 for _ in range(100)]
            stack=[]
            count=0
            stack.append((0,i))
            while stack:
                cr,cc=stack.pop()
                visited[cr][cc]=1
                for k in range(3):
                    nr=cr+dr[k]
                    nc=cc+dc[k]
                    if 0<=nr<100 and 0<=nc<100 and visited[nr][nc]==0 and ladder[nr][nc]==1:
                        stack.append((nr,nc))
                        if nr==99:
                            result[i]=count
                        count+=1
    return result


for tc in range(1,11):
    t=int(input())
    ladder=[list(map(int,input().split())) for _ in range(100)]
    print(ladder_check())