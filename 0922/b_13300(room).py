N,K=map(int,input().split()) # 학생수, 최대 인원수

rooms=[[0]*2 for _ in range(7)]
for _ in range(N):
    S,Y=map(int,input().split()) #성별(0-여자,1-남자), 학년
    rooms[Y][S]+=1

total=0
for i in range(1,len(rooms)):
    for j in range(2):
        if (rooms[i][j]%K==0):
            total+=rooms[i][j]//K
        else:
            total+=rooms[i][j]//K+1
print(total)

'''
9 5
0 3
1 1
0 3
0 3
0 3
0 3
0 3
0 3
0 3
'''