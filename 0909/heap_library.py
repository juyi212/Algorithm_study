#최소힙만 지원한다 (heapq)

import heapq
heap=[7,2,5,3,4,6] #list
print(heap)
heapq.heapify(heap) #최소힙으로 만들어줌
print(heap)
heapq.heappush(heap,1) #삽입
print(heap)

while heap:
    print(heapq.heappop(heap),end=' ') #오름차순으로 뽑혀서 만들어줌
print()



#####################################
#최대힙은 ?
temp=[7,2,5,3,4,6]
heap2=[]
for i in range(len(temp)):
    heapq.heappush(heap2,(-temp[i],temp[i])) #앞순서 먼저
heapq.heappush(heap2,(-1,1))
print(heap2)

while heap2:
    print(heapq.heappop(heap2)[1],end=' ')
    # print(heapq.heappop(heap2)*-1, end=' ')

