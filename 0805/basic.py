# arr=[[1,2,3],[4,5,6,7],[8,9]]
# sum=0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         sum+=arr[i][j]
# print(sum)

#팔방 시계방향 순회

arr=[[1,2,3],[4,5,6],[7,8,9]]
n=len(arr)
m=len(arr[0])
#상 우상 우 우하 하 좌하 좌 좌상
dr=[-1,-1,0,1,1,1,0,-1]
dc=[0,1,1,1,0,-1,-1,-1]

r=1
c=1
for i in range(8):
    nr=r+dr[i]
    nc=c+dc[i]
    print(arr[nr][nc])