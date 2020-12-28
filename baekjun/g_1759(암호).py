from itertools import combinations

L,C=map(int,input().split()) # 자리수, 알파벳수

amho=list(input().split())
# 최소 한 개의 모음과 두 개의 자음
# amho=sorted(list(input().split())) 시간이 좀 오래걸림

moum=['a','e','i','o','u']

a=sorted([ord(i) for i in amho])
b=[chr(i) for i in a]

result=list(map(''.join,combinations(b,L)))

for i in result:
    n=0
    for j in i:
        if j in moum:
            n+=1
    if n>0 and len(i)-n>1:
        print(i)


