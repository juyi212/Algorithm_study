N=10
A=[0]*N
arr=[1,2,3,4,5,6,7,8,9,10]
total=0

def printset(n,cursum):
    if cursum==10:
        for i in range(n):
            if A[i]==1:
                print(arr[i], end=' ')
        print()

    return 0


def powerset(n,k,cursum):
    if cursum>10:
        return
    if n==k:
        printset(n,cursum)
    else:
        A[k]=1
        powerset(n,k+1,cursum+arr[k])
        A[k]=0
        powerset(n,k+1,cursum)

powerset(N,0,0)