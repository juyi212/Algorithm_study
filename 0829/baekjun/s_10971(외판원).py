import sys
sys.setrecursionlimit(100000)

def dfs(node,s):
    global min_c
    if len(stack)==n: # 마지막 노드에서 처음으로 돌아가는 노드를 더해주기위해
        if cities_c[node][0] !=0:
            s+=cities_c[node][0]
            if s<min_c:
                min_c=s
    
    for w in range(n):
        if node!=w and not w in stack and cities_c[node][w] != 0:
            stack.append(w)
            if min_c>=s+cities_c[node][w]: # 비용을 더해준 값이 최소비용보다 크면 이후 노드는 할 필요가 없다.
                dfs(w,s+cities_c[node][w])
            stack.pop()

n=int(input())
cities_c=[list(map(int,input().split())) for _ in range(n)]

 # circle이라서 노드 하나만 봐도 됨. 고치자
min_c=100000000000
s=0
stack=[0]
dfs(0,0)
print(min_c)


# if value + cities[next][w] < min_value[0]:
#     dfs(start, w, value + cities[next][w], visited)

'''
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
'''

'''
9
0 10 15 20 1 1 1 1 1
5 0 9 10 1 1 1 1 1
6 13 0 12 1 1 1 1 1
8 8 9 0 1 1 1 1 1
8 8 9 1 0 1 1 1 1
8 8 9 0 1 0 1 1 1
8 8 9 0 1 1 0 1 1
8 8 9 3 1 1 1 0 1
8 8 9 4 1 1 1 1 0

28
'''