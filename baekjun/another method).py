import sys

def solution(arr,n,s):
    sumlist=[]

    for i in range(n):
        for j in range(len(sumlist)):
            sumlist.append(sumlist[j]+arr[i])
        sumlist.append(arr[i])
    return sumlist.count(s)


n,s=map(int,input().split())
numbers=list(map(int,input().split()))

print(solution(numbers,n,s))