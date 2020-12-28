#n,m=map(int,input().split())

#1
# mylist = [0]* n
# for i in range(n):
#     mylist[i]=list(map(int,input().split()))
# print(mylist)

#2
# n,m=map(int,input().split())
# mylist=[]
# for i in range(n):
#     mylist.append(list(map(int,input().split())))
# print(mylist)


#3 전치행렬
# n,m=map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(n)]
#
# for i in range(n):
#     for j in range(i+1,m):
#         #if i<j:
#             arr[i][j] , arr[j][i] = arr[j][i],arr[i][j]
# print(arr,end='')

# 1 2 3 4 2개씩 조합, 전치행렬 이용용arr=[1,2,3,4]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        print((arr[i],arr[j]),end='')


#4
# n=3 #행
# m=4 #열
# #열부터 만들어야 한다.
# v=[[0 for _ in range(m)]for _ in range(n)]
# v=[[0]*m for _ in range(n)]