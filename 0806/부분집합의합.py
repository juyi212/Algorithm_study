import sys
sys.stdin=open("sample_input_sum.txt","r")

T=int(input())
for test_case in range(1,T+1):
    n, k = map(int,input().split())
    numbers=list(range(1,13))
    x = []
    for i in range(1<<12):
        li = []
        for j in range(13):
            if i & (1<<j):
                li.append(numbers[j])
        x.append(li)
        count=0

    for j in x:
        if len(j) == n:
            sum_v = 0
            for l in j:
                sum_v += l
            if sum_v == k:
                count += 1
    print(f'#{test_case} {count}')

# if len(li) == n:
#     total = 0
# for z in li:
#     total+=z
# if total == k:
#     count+=1

#         values=random.sample(numbers,n)
#         for value in values:
#             sum+=value
#         if sum == k:
#             print(1)
#         fact-1
