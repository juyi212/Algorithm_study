n=int(input())
matrix=[[0]*101 for _ in range(101)]
for i in range(n):
    s,e=map(int,input().split())
    for x in range(e,e+10):
        for y in range(s,s+10):
            matrix[x][y]=1

total=0
for k in matrix:
    for j in k:
        if j==1:
            total+=1
print(total)

# def check(x,y):
#     global result
#     cnt_r=0
#     num=matrix[x][y]
#     for a in range(x,len(matrix)):
#         for b in range(y,len(matrix)):
#             if matrix[a][b]==num:
#                 cnt_r+=1
#             elif cnt_r > 0 and matrix[a][b] != num:
#                 q = a + 1
#                 w = b - 1
#                 cnt_c = 1
#                 while True:
#                     if matrix[q][w] == num:
#                         cnt_c += 1
#                         q += 1
#                     else:
#                         result += (cnt_c * cnt_r)
#                         return q,w
#
# color=int(input())
# matrix=[[0]*101 for _ in range(101)]
# for i in range(color):
#     x,y=map(int,input().split())
#     for a in range(y,y+10):
#         for b in range(x,x+10):
#             matrix[a][b]+=1
#
# result=0
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if matrix[i][j]>1:
#             q,w=check(i,j)
#             for n in range(i,q+1):
#                 for m in range(j,w+1):
#                     matrix[n][m]=1
# print(result)
# print((100*color)-result)

'''
3
10 10
10 10
10 10
'''
