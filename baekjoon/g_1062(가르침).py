import sys

# 시간 초과
# def check_char(idx, cnt):
#     global answer
#     if idx >= len(checkit):
#         return
#     if cnt == 0:
#         new_char = []
#         for i in range(len(checkit)):
#             if checkit[i]:
#                 new_char.append(character[i])
#
#         cntcnt = 0
#         new_word = my_st + new_char
#         for ch in words:
#             for c in ch:
#                 if c in new_char:
#                     cntcnt += 1
#         answer = max(answer, cntcnt)
#
#
#     checkit[idx] = True
#     check_char(idx+1, cnt-1)
#     checkit[idx] = False
#     check_char(idx+1, cnt)
#
#
# N, K = map(int, sys.stdin.readline().split()) # 단어의 개수, 읽을 수 있는 문자의 수
# # a n t i c => anta~~~tica 적어도 글자를 읽으려면 5개 이상이어야함
#
# if K < 5:
#     print(0)
# else:
#     cnt = K-5
#     my_st = ['a','n','t','i','c']
#     words =[]
#     character = []
#     for i in range(N):
#         word = sys.stdin.readline().rstrip()
#         chars = list(word[4:-4])
#         words.append(list(chars))
#         for j in chars:
#             if j not in my_st and j not in character:
#                 character.append(j)
#
#     answer = -1
#     checkit = [False] * len(character)
#     check_char(0, cnt)
#     print(answer)

# 시간초과.. 비트마스킹 아니면 시간이 또이또이 함
# pypy3 로 제출
def check(idx, cnt):
    global answer

    if cnt == 0:
        read_cnt = 0
        for word in words:
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    break
            else:
                read_cnt += 1
        answer = max(answer, read_cnt)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            check(i, cnt-1)
            learn[i] = False


N, K = map(int, sys.stdin.readline().split())  # 단어의 개수, 읽을 수 있는 문자의 수
# a n t i c => anta~~~tica 적어도 글자를 읽으려면 5개 이상이어야함

if K < 5:
    print(0)
else:
    cnt = K - 5
    words = [set(sys.stdin.readline().rstrip()) for _ in range(N)]
    # combination?????
    learn = [False] * 26
    for c in ('a','c','t','i','n'):
        learn[ord(c) - ord('a')] = True
    answer = -1
    check(0, cnt)
    print(answer)


#
# from itertools import combinations
# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# default = set(list('antatica'))
# chars = set()
# cnt = len(default)
#
# if cnt > k:
#     print(0)
#     exit(0)
#
# arr = []
# result = 0
#
# for i in range(n):
#     word = list(sys.stdin.readline())
#     tmp = set(word[4:len(word)-4]) - default
#     if len(tmp) + cnt <= k:
#         arr.append(tmp)
#         chars.update(tmp)
#         result = 1
#
# n = len(arr)
# if result == 0:
#     print(0)
#     exit(0)
#
# if len(chars) <= k - cnt:
#     result = len(arr)
# else:
#     tmp = list(combinations(chars, k - cnt))
#     for t in tmp:
#         t = set(list(t))
#         c = 0
#         for a in arr:
#             if not (a - t):
#                 c += 1
#         result = max(result, c)
#
#
# print(result)