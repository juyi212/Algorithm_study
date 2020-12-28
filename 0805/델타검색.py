arr=[[1,2,3,4]
     ,[5,6,7,8]
     ,[9,10,11,12]
     ]
n=len(arr)
m=len(arr[0])

dr=[-1,1,0,0]
dc=[0,0,-1,1]

for x in range(n):
    for y in range(m):
        for i in range(4): #4방향이기때문에
            testX = x + dr[i]
            testY = y + dc[i]
            if testX >=0 and testX < n and testY>=0 and testY<m: #인덱스 체크
                print(arr[testX][testY], end=' ')

#상하좌우로 연속으로 순회하기

#4방향으로 나누기 4
