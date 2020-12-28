import sys
sys.stdin=open("sample_input_search.txt","r")

def binarysearch(P,C):
    start = 1
    count=0
    while start<=P:
        middle=int((start+P)/2)
        if middle == C:
            count+=1
            return count
        elif middle < C:
            start=middle
            count+=1
        else:
            P=middle
            count+=1

T=int(input())
for test_case in range(1,T+1):
    P,A,B= map(int,input().split())
    PA=binarysearch(P,A)
    PB=binarysearch(P,B)
    if PA<PB:
        print(f'#{test_case} A')
    elif PA>PB:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')