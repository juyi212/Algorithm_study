import sys

sys.stdin = open('input1.txt','r')

T=int(input())
for i in range(0, T):
    day = int(input())
    dayprice = list(map(int, input().split()))
    maxprice = dayprice[len(dayprice)-1]
    benefit = 0
    buy = 0
    for j in range(day-2, -1, -1):
        if dayprice[j] < maxprice:
            benefit += maxprice-dayprice[j]
        else:
            maxprice = dayprice[j]
    print('#{0} {1}'.format(i+1, benefit))



# for tc in range(1, int(input())+1):
#     N = int(input())
#     costs = list(map(int, input().split()))
#
#     result = 0
#     while True:
#         max_value = max(costs)
#         max_idx = costs.index(max_value)
#         total = 0
#         if max_idx != 0:
#             total = max_value * max_idx
#             for i in range(max_idx):
#                 total -= costs[i]
#             result += total
#
#         if max_idx == len(costs)-1 or max_idx == len(costs)-2:
#             break
#         else:
#             costs = costs[max_idx+1:]
#
#     print(f'#{tc} {result}')

