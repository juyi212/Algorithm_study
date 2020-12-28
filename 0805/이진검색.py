def binarySearch(a,key):
    start=0
    end=len(a)
    while start<= end:
        middle=(start +end)//2
        #key값이 같은 경우, 작은경우, 큰경우
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle -1
        else:
            start=middle +1

    return False, -1

arr=[2,4,7,9,11,19,23]
key=17
print(binarySearch(arr,key))