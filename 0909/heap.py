def heappush(value):
    global heapcount
    heapcount+=1
    heap[heapcount]=value
    cur=heapcount #idx 번호
    parent=cur//2 #2일때 1번 idx
    #루트가 아니고, if 부모 노드값>자식 노드 값 -> swap
    while parent and heap[parent]>heap[cur]:
        heap[parent],heap[cur]=heap[cur],heap[parent]
        cur=parent
        parent=cur//2

def heappop():
    global heapcount
    retValue= heap[1] #루트를 리턴해야함
    heap[1]=heap[heapcount] #복사를 해둠
    heap[heapcount]=0 #지우기
    heapcount-=1

    parent=1
    child=parent*2 #왼쪽자식
    if child+1 <= heapcount: #오른쪽이 존재한다는 것임.
        if heap[child] > heap[child+1]: #오른쪽이 더 작으면 바꾸자
            child=child+1
    #자식 노드가 존재하고, 부모 노드>자식노드  = swap
    while child <= heapcount and heap[parent]>heap[child]:
        heap[parent],heap[child] = heap[child],heap[parent]
        parent=child
        child = parent*2
        if child + 1 <= heapcount:
            if heap[child] > heap[child + 1]:
                child = child + 1
    return retValue

# 최소힙
heapcount=0
temp=[7,2,5,3,4,6] #하나씩 빼서 heap에 넣을 것임
N=len(temp)
heap=[0]*(N+1)

for i in range(N):
    heappush(temp[i])

for i in range(N):
    print(heappop(),end=' ')
print()
