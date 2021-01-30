import sys
from collections import deque

def check(n, k, conveyor):
    global cnt
    q = deque(conveyor)

    while q:
        # 순서대로 해야한다 주이야^^
        cnt += 1
        if robot[n - 1]:
            robot[n - 1] = False
        # 컨베이어를 돌려
        end = q.pop()
        q.insert(0, end)

        # 로봇도 돌려
        r_end = robot.pop()
        robot.insert(0, r_end)

        # 마지막 다시 확인
        if robot[n - 1]:
            robot[n - 1] = False

        # 로봇이 컨베이어 벨트에서 움직일 수 있는 경우
        for i in range(n-2, -1, -1):
            if robot[i]:
                if not robot[i+1] and q[i+1] > 0:
                    robot[i+1] = True
                    robot[i] = False
                    q[i+1] -= 1

        # 처음에 없으면 넣어줘
        if q[0] > 0 and not robot[0]:
            robot[0] = True
            q[0] -= 1

        if q.count(0) >= k:
            return cnt


n, k = map(int, sys.stdin.readline().split())
conveyor = list(map(int, sys.stdin.readline().split()))
robot = [False] * n
cnt = 0
check(n, k, conveyor)
print(cnt)
