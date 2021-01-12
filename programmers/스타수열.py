from collections import Counter

def solution(a):
    elements = Counter(a)
    # 공통원소 하나 이상 들어가면 됨
    # 양옆만 보는게 아님
    answer = -1
    for num in elements.keys():
        if elements[num] <= answer:
            continue
        tmp = []
        left, right = 0, 1
        while right < len(a):
            if (num == a[left] or num == a[right]) and a[left] != a[right]:
                tmp.append((a[left], a[right]))
                left = right + 1
            else:
                right += 1

        answer = max(answer, len(tmp))

    if answer == -1:
        return answer
    else:
        return answer*2



a = [5, 2, 3, 3, 5, 3]
print(solution(a))


# 규태
# def solution(a):
#     answer = 0
#
#     visited = {}
#
#     i = 0
#     while i < len(a):
#         if a[i] in visited:
#             if 0 <= i - 1 and i - 1 not in visited[a[i]] and a[i - 1] != a[i]:
#                 visited[a[i]].add(i - 1)
#             elif i + 1 < len(a) and a[i + 1] != a[i]:
#                 visited[a[i]].add(i + 1)
#         else:
#             visited[a[i]] = set()
#             if 0 <= i - 1 and i - 1 not in visited[a[i]] and a[i - 1] != a[i]:
#                 visited[a[i]].add(i - 1)
#             elif i + 1 < len(a) and a[i + 1] != a[i]:
#                 visited[a[i]].add(i + 1)
#         i += 1
#
#     for i in visited:
#         answer = max(answer, len(visited[i]))
#
#     return answer * 2

# 승한
# def solution(a):
#     answer = -1
#     N = len(a)
#
#     if N <= 1:
#         return 0
#
#     counter = [0] * (N + 1)
#     limit = [-1] * (N + 1)
#     for idx, k in enumerate(a):
#         if limit[k] >= idx:
#             continue
#
#         if limit[k] < idx - 1:
#             limit[k] = idx
#             counter[k] += 1
#         elif limit[k] == idx - 1 and idx + 1 < len(a):
#             if a[idx + 1] != k:
#                 limit[k] = idx + 1
#                 counter[k] += 1
#             else:
#                 limit[k] = idx
#
#     answer = max(counter) * 2
#
#
#     return answer