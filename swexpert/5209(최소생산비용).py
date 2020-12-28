
def dfs(v, total):
    global min_c

    if v == n:
        if total < min_c:
            min_c = total
            return


    else:
        for j in range(n):
            if not visited[j]:
                visited[j] = True
                if min_c > total + matrix[v][j]:
                    dfs(v+1, total + matrix[v][j])
                visited[j] = False


for tc in range(1, int(input())+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    min_c = 10000000
    dfs(0, 0)
    print('#{} {}'.format(tc, min_c))