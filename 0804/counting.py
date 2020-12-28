import sys
sys.stdin=open('sample_input.txt','r')

def countingsort(a,b):
    c=[0]*11
    for i in range(len(b)):
        c[a[i]]+=1 #인덱스가 번호 벨류는 count 수

    print(c)

    max_v=c[0]
    max_idx=0
    for i in range(len(c)):
        if c[i]>=max_v:
            max_v=c[i] #인덱스 번호가 이미 배열이 되어있으니
            max_idx=i   #같을 경우에는 가장 뒤에 있는 번호가 저장됨.
    return f'#{test_case} {max_idx} {max_v}'

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = input()
    li=[]
    for i in a:
        li.append(int(i))
    b=[0]*len(li)
    print(countingsort(li,b))