def quicksort(arr, low, high):
    if low < high:
        i = low-1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        print(*arr)
        quicksort(arr, low, i-1)
        quicksort(arr, i + 1, high)

n = int(input())
arr = list(map(int, input().split()))

quicksort(arr, 0, n-1)