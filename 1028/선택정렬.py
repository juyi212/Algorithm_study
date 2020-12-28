# def selectionsort(a):
#     n = len(a)
#
#     for i in range(0, n-1):
#         min = i
#         for j in range(i+1, n):
#             if a[j] < a[min]:
#                 min = j
#         a[min], a[i] = a[i], a[min]
#
#
# a = [1, 5, 4, 3, 6]
# selectionsort(a)
# print(a)
#   선택 정렬 함수를 재귀적 알고리즘으로 구현하시오.

def selectionsort(a, s):
    n = len(a)
    if s == n-1:
        return
    min = s
    for i in range(s, n):
        if a[min] > a[i]:
            min = i
    a[s], a[min] = a[min], a[s]

    selectionsort(a, s+1)


a = [1, 5, 4, 3, 6]
selectionsort(a, 0)
print(a)