# def even(i,j,k):
#     color=colors[(i%3)-1]
#     matrix[i][j]=color
#     nx=i
#     ny=j
#     for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
#         nx+=dr
#         ny+=dc
#         if 0<nx<=N//2+(2*k) and 0<ny<=N//2+(2*k):
#             while True:
#                 if nx<i or nx>=i+(2*k) or ny<j or ny>=j+(2*k):
#                         nx-=dr
#                         ny-=dc
#                         break
#                 elif nx==i and ny==j:
#                     return
#                 else:
#                     matrix[nx][ny]=color
#                     nx+=dr
#                     ny+=dc
#
# def odd(i,j,k):
#     color=colors[(i%3)-1]
#     matrix[i][j]=color
#     nx=i
#     ny=j
#     for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
#         nx+=dr
#         ny+=dc
#         if 0<nx<=N//2+((2*k)+1) and 0<ny<=N//2+((2*k)+1):
#             while True:
#                 if nx<i or nx>=i+(2*k+1) or ny<j or ny>=j+(2*k+1):
#                         nx-=dr
#                         ny-=dc
#                         break
#                 elif nx==i and ny==j:
#                     return
#                 else:
#                     matrix[nx][ny]=color
#                     nx+=dr
#                     ny+=dc
N=int(input())
k=int(input()) #제거한 타일의 개수

for i in range(k):
    a,b=map(int,input().split())
    if N//2<a: #한방향으로 다 보내줌
        a=N+1-a
    if N//2<b:
        b=N+1-b
    r=min(a,b)
    if r%3==0:
        print(3)
    else:
        print(r%3)




# cnt_e=0
# cnt_0=0
# for i in range(N//2,0,-1):
#     even(i,i,cnt_e)
#     cnt_e+=1
# else:
#     for i in range(N//2+1,0,-1):
#         odd(i,i,cnt_0)
#         cnt_0+=1

