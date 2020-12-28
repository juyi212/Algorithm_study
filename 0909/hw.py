def inorder(idx):
    if idx>V:
        return
    inorder(idx*2)
    print(matrix[idx],end='')
    inorder(idx*2+1)

for tc in range(1,11):
    V=int(input())#정점
    E=V-1 #간선
    matrix=[0]*(V+1)
    for i in range(1,V+1):
        temp=input().split()
        matrix[int(temp[0])]=temp[1] #왼오,짝홀
    print(f'#{tc}',end=' ')
    inorder(1)
    print()
'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S

'''