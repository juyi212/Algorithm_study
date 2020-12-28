import sys
sys.stdin=open("input.txt","r")

def search(n):
    number = list(range(1, 10))
    arr = []
    for i in n: #행-> 열
        ri = [0] * 9
        for j in range(9):
            if i[j] in number:
                ri[i[j] - 1] += 1
        arr.append(ri)
    for a in arr:
        for i in a:
            if i != 1:
                return f'#{test_case} 0'

    arr = [] #열->행
    for c in range(len(n)):
        ri = [0]*9
        for i in n:
            if i[c] in number:
                ri[i[c] - 1] += 1
        arr.append(ri)
    for a in arr:
        for i in a:
            if i != 1:
                return f'#{test_case} 0'

    arr=[] #사각형 합
    for nr in range(0,9,3):
        for nc in range(0,9,3):
            ri = [0] * 9
            for sr in range(3):
                for sc in range(3):
                    if n[nr+sr][nc+sc] in number:
                        ri[n[nr+sr][nc+sc]- 1] += 1
            arr.append(ri)
    for a in arr:
        for i in a:
            if i != 1:
                return f'#{test_case} 0'
    return f'#{test_case} 1'
T=int(input())
for test_case in range(1,T+1):
    n=[]
    for i in range(9):
        n.append(list(map(int,input().split())))
    print(search(n))
