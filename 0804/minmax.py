import sys
sys.stdin=open('sample_input.txt','r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split( )))
    max_num=a[0]
    min_num=a[0]
    for i in a:
        if max_num<i:
            max_num=i
    for j in a:
        if min_num>j:
            min_num=j
    print(f'#{test_case} {max_num-min_num}')