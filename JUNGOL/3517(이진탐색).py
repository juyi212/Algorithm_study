def binarySearch1(nli, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if nli[mid] == target:
            return mid
        if nli[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binarySearch2(nli, low, high, target):
    if low > high:
        return -1
    mid = (low+high)//2

    if nli[mid] == target:
        return mid
    if nli[mid] > target:
        return binarySearch2(nli, low, mid-1, target)
    return binarySearch2(nli, mid+1, high, target)


n = int(input())
nli = list(map(int, input().split()))

q = int(input())
qli = list(map(int, input().split()))

for i in range(q):
    print(binarySearch2(nli, 0, len(nli), qli[i]), end=' ')
