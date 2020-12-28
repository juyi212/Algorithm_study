import sys
#   퀵정렬
#   파티션 : 피벗을 하나 정해서, 큰 값과 작은 값들로 구분
#   재귀호출 부분 : 큰 값과 작은 값의 부분들을 각각 다시 퀵정렬 호출


def quick_sort(arr, left, right):

    if left < right:
        # 파티션 나누고
        pivot = partition(arr, left, right)
        # 왼쪽 부분 호출
        quick_sort(arr, left, pivot-1)
        # 오른쪽 부분 호출
        quick_sort(arr, pivot+1, right)


def partition(arr, left, right):
    # 피벗잡고
    # 피벗보다 작은 값을 앞쪽으로
    # 피벗보다 큰 값을 뒤쪽으로
    i = left
    j = right
    pivot = arr[left]

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[left] = arr[left], arr[j]   # pivot 과 j 위치를 바꿔줌
    return j    # pivot  위치 반환


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
    print('#{} {}'.format(tc, arr[N//2]))