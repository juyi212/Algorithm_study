import sys
import ast
from collections import deque

for _ in range(int(sys.stdin.readline())):
    func = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline()) # 배열 길이
    li = sys.stdin.readline().strip()
    li = ast.literal_eval(li) # 문자열 속 표현식 인식하게 해주는 라이브러리
    # matrix = matrix.replace('[','')
    # matrix = matrix.replace(']','')
    # if len(matrix) != 0:
    #     li = list(map(int, matrix.split(',')))
    # else:
    #     li = []
    q = deque(li)
    check = 0

    for v in func:
        if v == 'R':    # 방향 바꾸기
            if check == 0:
                check = 1
            elif check == 1:
                check = 0

        if v == 'D':
            if len(q) == 0: # 빈배열
                check = 2
                break
            if check == 0:  # 정방향 두번 뒤집힌경우 또는 안 뒤집힌경우
                q.popleft()
            elif check == 1:    # 역방향   # 한번 뒤집힌 경우
                q.pop()

    if check == 1:
        q.reverse()
    if check == 2:
        print('error')
    else:
        print('[', end='')
        for i in range(len(q)):
            print(q[i], end='')
            if i != len(q)-1:
                print(',', end='')
        print(']')