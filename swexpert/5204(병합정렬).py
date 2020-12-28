# # merge sort
# # n/2 나누고, 1개씩의 요소가 남기까지 재귀적으로 conquer 한다
# # 그 후, 그 다음에 2개씩의 요소들을 반복적으로 merge 한다.
#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]
#
#     left1 = merge_sort(left)
#     right1 = merge_sort(right)
#     return merge(left1, right1)
#
#
# def merge(left, right):
#     global cnt
#     i = 0
#     j = 0
#     sorted_arr = []
#
#     if left[-1] > right[-1]:
#         cnt += 1
#
#     while (i < len(left)) & (j < len(right)):
#         if left[i] < right[j]:
#             sorted_arr.append(left[i])
#             i += 1
#         else:
#             sorted_arr.append(right[j])
#             j += 1
#
#     while i < len(left):
#         sorted_arr.append(left[i])
#         i += 1
#
#     while j < len(right):
#         sorted_arr.append(right[j])
#         j += 1
#
#     return sorted_arr
#
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     a = merge_sort(arr)
#     print(a)
#     print(f'#{tc} {a[N//2]} {cnt}')


# O(nlogn) 병합정렬
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr)//2

    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])

    return merge(left, right)


def merge(left, right):  # left, right 를 병합
    result = list()

    i = j = 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
        elif j < len(right):    # 왼쪽 배열은 다 복사되고, 오른쪽이 남아있을경우
            result.append(right[j])
            j += 1
        elif i < len(left):
            result.append(left[i])
            i += 1

    return result



    return result



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = [0]
    print(merge_sort(arr))





# def sum_sort(array):
#
#     if len(array) <= 1:
#         return array
#
#     c = len(array)//2
#     l_array = sum_sort(array[:c])
#     r_array = sum_sort(array[c:])
#
#     if l_array[-1] > r_array[-1]:
#         cnt[0] += 1
#
#     new_array = []
#     i = 0
#     j = 0
#     l_len = len(l_array)
#     r_len = len(r_array)
#     while len(new_array) < l_len + r_len:
#
#         if i == l_len:
#             new_array.append(r_array[j])
#             j += 1
#         elif j == r_len:
#             new_array.append(l_array[i])
#             i += 1
#         elif l_array[i] < r_array[j]:
#             new_array.append(l_array[i])
#             i += 1
#         else:   # l_array[i] >= r_array[j]
#             new_array.append(r_array[j])
#             j += 1
#
#     return new_array



    # result = sum_sort(numbers)
    # print(result)
    # print('#{} {} {}'.format(t, result[N//2], cnt[0]))


'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''