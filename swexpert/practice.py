def check(x, y, k):
    arr = [[0]*k for _ in range(k)]

    for i in range(k):
        for j in range(k):
            arr[i][j] = matrix[i+y][j+x]

    for i in range(k):
        for j in range(k):
            matrix[j+y][k-i+x-1] = arr[i][j]



for tc in range(1, int(input())+1):
    N, C, X, Y, K, R = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    if X+K > N+1 and Y+K > N+1:
        print(-1)
    else:
        for _ in range((C % 360)//90):
            check(X-1, Y-1, K)
        print(matrix)


'''
1
5 180 2 3 3 3 
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 

'''


