import sys
sys.stdin = open('input13.txt', 'r')


def dfs(s1, e1, total):
    global min_dis

    if False not in visited:
        total += abs(s1-x2)+abs(e1-y2)
        if total < min_dis:
            min_dis = total
            return


    else:
        for i in range(0, n):
            if not visited[i]:
                visited[i] = True
                s2,e2 = matrix[i*2], matrix[i*2+1]
                if min_dis > total + abs(s1-s2)+abs(e1-e2):
                    dfs(s2,e2, total + abs(s1-s2)+abs(e1-e2))
                visited[i] = False


for tc in range(1, int(input())+1):
    n = int(input())
    x1,y1, x2, y2, *matrix = map(int, input().split())  # 회사, 집, 고객
    min_dis = 100000000
    visited = [False] * n
    dfs(x1, y1, 0)
    print('#{} {}'.format(tc, min_dis))