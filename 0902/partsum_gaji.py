N=10
A=[0]*N
arr=[1,2,3,4,5,6,7,8,9,10]
total=0

def printSet(n,sum):
    global count
    if sum==10:
        for i in range(n):
            if A[i]==1:
                print(arr[i], end=' ')

        print()

def powerset(n,k,cursum): # n 원소의 갯수, k 현재 depth
    global total
    if cursum >10:
        return
    total+=1

    if n==k:
        printSet(n,cursum)
    else:
        A[k]=1
        powerset(n,k+1,cursum+arr[k])
        A[k]=0
        powerset(n,k+1,cursum)

powerset(N,0,0)
print(f'가지치기 {total}')