def BruteForce(p,t):
    i=0 # t의 인덱스
    j=0 # p의 인덱스

    while j <m and i <n :
        if t[i]!=p[j]:
            i=i-j
            j=-1
        i+=1
        j+=1
    if j==m : reutrn i-m # 검색성공 
    else: return -1

p='is' # 찾을 패턴
t= 'This is a book~!' # 전체 텍스트
m=len(p)
n=len(t)