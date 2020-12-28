import sys

N, M = map(int, sys.stdin.readline().split()) # 덩어리의 개수, 필요한 고기 양

meats = []
for i in range(N):
    w, c = map(int, sys.stdin.readline().split()) # 무게와 가격
    meats.append([w, c])

meats.sort(key=lambda x:(x[1], -x[0])) # 가격 기준으로 오름차순, 무게 내림
same = 0

# 가격은 더 싼데 고기양이 더 많을 수도 있다.
# 무게가 같으면 가격을 다 더해준다.

total, answer = 0, float('inf')
stop = False  

for i in range(N):
    total += meats[i][0]
    if i >= 1 and meats[i-1][1] == meats[i][1]:
        same += meats[i][1]
    else:
        same = 0
    if total >= M:
        stop = True
        answer = min(answer, meats[i][1]+same)

if stop:
    print(answer)
else:
    print(-1)




'''
4 3
1 2
3 2
2 2
5 2
'''

'''
10 10
2 3
2 4
2 5
3 1
1 3
7 9
7 3
8 4
10 3
3 10
'''