import sys
sys.stdin=open('sample_input_sum.txt','r')

for test_case in range(1,11):
    T = int(input())
    a = list(map(int, input().split()))
    while T>0:
        b=max(a)
        a.remove(b)
        a.append(b-1)

        c=min(a)
        a.remove(c)
        a.append(c+1)
        T-=1
    print(f'#{test_case} {max(a)-min(a)}')


# for i in range(T):
#     max_idx=0
#     min_idx=0
#     max_v=area[0]
#     min_v=area[0]
#     for j in range(len(area)):
#         #최대값 위치, 최소값 위치
#         if area[j]>max_v:
#             max_idx=j
#             max_v=area[j]
#         if area[j]<min_v:
#             min_idx=j
#             min_v=area[j]
#








