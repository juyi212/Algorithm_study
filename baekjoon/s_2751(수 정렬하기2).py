

# 시간복잡도 nlonn -> 힙정렬, 병합정렬, 퀵정렬 등으로 풀어야함.
# sys.stdin... 이거 차이큼
# 시간초과는 안나지만 효율성은 좀 떨어짐

import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()
print("\n".join(list(map(str, li)))) # 하나씩 출력해줌

# for a in li:
#     print(a)

