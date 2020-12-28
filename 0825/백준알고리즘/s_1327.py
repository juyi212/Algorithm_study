import sys

n,k=map(int,input().split())
arr=sys.stdin.readline().split()
a=arr[::]

a.sort()
result=arr[::]
result.sort()
count=0
queue=[0]*n

num=0
while num<40732:
    for i in range(len(arr)-(k-1)):
        count += 1
        num+=1
        blank=arr[i:i+k]
        blank.reverse()
        for j in range(k):
            arr.pop(i+j)
            arr.insert(i+j,blank[j])

        if arr[-1]==a[-1]:
            queue[len(arr)-1]=arr[-1]
            arr.pop()
            a.pop()
            break

    if arr == a:
        for i in range(len(arr)):
            queue[i] = arr[i]
        if result == queue:
            print(count)
            break
else:
    print(-1)