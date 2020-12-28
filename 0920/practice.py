#### 부분집합

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
for i in range(1<<n):
    for j in range(n+1):
        if i & (1<<j):
            print(arr[j], end=", ")
    print()
print()


#### dfs
T = int(input())
for tc in range(1, T+1):
    def dfs(v):
        # visited[v] = 1
        # for w in range(1, N + 1):
        #     if matrix[v][w] == 1 and visited[w] == 0:
        #         dfs(w)

        stack = list()
        stack.append(v)
        visited[v] = 1 
        while stack:
            current = stack[-1]
            visited[current] = 1
            for i in range(len(matrix[current])):
                if matrix[current][i] == 1 and visited[i] == 0:
                    stack.append(i) 
                    break
            else:
                stack.pop()

    result = []
    N, E = map(int, input().split())
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)

    for i in range(E):
        s, e = map(int, input().split())
        # 단방향
        matrix[s][e] = 1
    S, G = map(int, input().split())

    dfs(S)
    if visited[G] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


#### bfs
def bfs(S):
    visited = [0]*(V+1)
    queue = [(S, 0)]
    visited[S] = 1
    while queue:
        s, cnt = queue.pop(0)
        if s == G:
            return cnt
        for e in range(V+1):
            if matrix[s][e] != 0 and visited[e] == 0:
                queue.append((e, cnt + 1))
                visited[s] = 1
    return 0

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        matrix[x][y] = 1
        matrix[y][x] = 1
    S, G = map(int, input().split())
    print(f'#{tc+1} {bfs(S)}')


#### N-Queen
N = 10
check = [[0] * N for _ in range(N)]
cnt = 0
def marking(r, c, num):
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for d in range(8):
        nr = r
        nc = c
        while True:
            nr += dr[d]
            nc += dc[d]
            if 0 > nr or 0 > nc or nr >= N or nc >=N:
                break
            check[nr][nc] += num

def n_queen(r):
    global cnt
    if r >= N:
        cnt += 1
        return
    for i in range(N): 
        if check[r][i] == 0:    
            marking(r, i, 1)
            n_queen(r+1)
            marking(r, i, -1)
    return

n_queen(0)
print(cnt)

arr = [1, 2, 3]
N = len(arr)
selected = [0] * N


#### powerset
def powerset(idx):
    if idx == N:
        for i in range(N):
            if selected[i] == 1:
                print(arr[i], end=' ')
        print()
        return
    selected[idx] = 1
    powerset(idx + 1)
    selected[idx] = 0
    powerset(idx + 1)
    
powerset(0)


#### permutation(순열)
arr = [1, 2, 3]
N = len(arr)


def perm(idx):
    if idx >= N:
        print(arr)
        return
    for i in range(idx, N):
        arr[i], arr[idx] = arr[idx], arr[i]
        perm(idx+1)
        arr[i], arr[idx] = arr[idx], arr[i]
perm(0)

#### 조합
N = 5
selected = [0] * N
T = 3

def comb(selected, idx, cnt):
    if cnt == T:    # 필요한 개수만큼 선택함
        print(selected)
        return
    if idx >= N:    # 범위 벗어남
        return
    selected[idx] = 1
    comb(selected, idx+1, cnt+1)
    selected[idx] = 0
    comb(selected, idx+1, cnt)

comb(selected, 0, 0)


#### 트리 생성 및 순회
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
def in_order(node):
    global cnt
    if node:
        cnt += 1
        in_order(tree[node][0])
        print(node, end=" ")
        in_order(tree[node][1])


V = int(input())    # 정점
E = V - 1   # 간선
tree = [[0] * 3 for _ in range(V + 1)]  # 14 * 3
temp = list(map(int, input().split()))
cnt = 0
for i in range(E):
    p, c = temp[i*2], temp[i*2+1]
    if tree[p][0] == 0:
        tree[p][0] = c  # left
    else:
        tree[p][1] = c  # right
    tree[c][2] = p      # parent
print(tree)

in_order(1)
print()
print(cnt)


#### 최소힙
def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur // 2

    # 루트가 아니고, if 부모노드값 > 자식노드값 => swap
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


def heappop():
    global heapcount
    retValue = heap[1]
    heap[1] = heap[heapcount]
    heap[heapcount] = 0
    heapcount -= 1
    parent = 1
    child = parent * 2

    if child + 1 <= heapcount:  # 오른쪽 자식 존재
        if heap[child] > heap[child+1]:
            child = child + 1
    # 자식노드가 존재하고, 부모노드 > 자식노드 => swap
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:  # 오른쪽 자식 존재
            if heap[child] > heap[child + 1]:
                child = child + 1
    return retValue


heapcount = 0
temp = [7, 2, 5, 3, 4, 6]
N = len(temp)
heap = [0] * (N + 1)
for i in range(N):
    heappush(temp[i])

for i in range(N):
    print(heappop(), end=" ")
print()


#### 퀵 정렬
# 피벗을 정하고 피벗보다 작은값으 앞쪽으로
# 피벗보다 큰값을 뒤쪽으로 보내면, 피벗의 위치가 결정됨
# 나누어진 부분을 다시 피벗을 기준으로 정리하면 계속해서
# 피벗의 위치가 결정되기 때문에 끝까지 진행하면, 정렬이 완료된다.
# 퀵정렬의 두 가지 작업
# 파티션 : 전체를 두 부분으로 나누는 작업
# 퀵정렬 : 나누어진 두 각각 부분을 다시 퀵정렬
def partition(arr, start, end):
    # 피벗 선택하고, 제일 앞쪽 값을 피벗으로 설정(피벗은 달라질 수 있다)
    pivot = arr[start]
    # 피벗보다 작으면 앞쪽으로, 크면 뒤쪽으로 보내기
    # [2][5][5][1][8][3][6][4][9]
    left = start + 1    # 피벗을 검사할 필요없음
    right = end
    while left <= right:    # left가 right보다 커지면 종료
        # left가 오른쪽으로 이동하며, 피벗보다 큰값을 찾기
        while left <= right and arr[left] <= pivot:
            left += 1
        # right가 왼쪽으로 이동하며, 피벗보다 작은값을 찾기
        while left <= right and arr[right] >= pivot:
            right -= 1

        # 각각 큰값과 작은값을 찾았으면, 위치교환
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    # 피벗을 제외하고, 피벗보다 작으면 왼쪽, 피벗보다 크면 오른쪽에 위치
    arr[start], arr[right] = arr[right], arr[start]

    return right    # 피봇 위치 반환

def quick_sort(arr, start, end):
    # 파티션을 실행하고,
    # 파티션으로 나누어진 부분을 각각 다시 퀵 소트
    pivot = partition(arr, start, end)
    quick_sort(arr, start, end)
    quick_sort(arr, pivot+1, end)


tree = [1, 2, 3, 4, 5]
##### 전위순회
def pre_order(idx):
    if idx >= len(tree):
        return
    if tree[idx] != -1:
        print(tree[idx], end=' ')
        pre_order(idx*2)
        pre_order(idx*2 + 1)

##### 중위 순회
def in_order(self, idx):
    if idx >= len(tree):
        return
    if tree[idx] != -1:
        in_order(idx*2)
        print(tree[idx], end=' ')
        in_order(idx*2 + 1)

##### 후위 순회
def post_order(idx):
    if idx >= len(tree):
        return
    if tree[idx] != -1:
        post_order(idx*2)
        post_order(idx*2 + 1)
        print(tree[idx], end=' ')

##### height

def f1(n,g,K,m): #n 고려할 직원 번호, g 직원 수, K 선반 높이, m은 n-1번까지 만들어진 탑의 높이
    global minV


    if n==g:
        if m>=K and minV>m-K:
            minV=m-K
    elif m>=K and minV <= m-K: #고려할 직원이 남아 있지만 탑의 높이가 기존보다 높은 경우
        return # 더 갈 이유가 x 그 이전에서 다른 선택하자
    else:
        f1(n+1,g,K,m)# n번 탑에 참여하지 않음 (이전 직원까지의 높이 m이 그대로 유지)
        f1(n+1,g,K,m+H[n]) #n-1까지의 높이 m + H[n] n번 직원의 높이 더해줌

t=int(input())
for tc in range(1,t+1):
    N,K=map(int,input().split()) # N은 직원수, K 선반 높이
    H=list(map(int,input().split()))
    A=[0]*N #탑에 포함되었는지 표시하기 위함
    minV=10000000
    f(0,N,K)
    # f1(0,N,K,0)
    print(minV)



#### ship

import sys
sys.setrecursionlimit(50000)

def dfs(i,j):
    checked[i][j]=1
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    for k in range(4):
        dx=i+dr[k]
        dy=j+dc[k]
        if 0>dx or m<=dx or 0>dy or dy>=n:
            continue
        if baba[dx][dy]==1 and not checked[dx][dy]:
            dfs(dx,dy)

t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    baba=[[0]*n for _ in range(m)]
    checked=[[0]*n for _ in range(m)]
    num=0
    for i in range(k):
        r,c=map(int,input().split())
        baba[r][c]=1

    for i in range(m):
        for j in range(n):
            if baba[i][j]==1 and not checked[i][j]:
                dfs(i,j)
                num += 1
    print(num)