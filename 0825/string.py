# import sys
# sys.stdin = open("sample_input.txt", "r")

def search(str1,str2):
    i=0 # 긴 문장
    j=0 # 찾을 문장 index
    m=len(str1) #찾을 문장
    n=len(str2) # 긴문장
    while i<n and j<m:
        if str2[i]!=str1[j]:
            i=i-j
            j=-1
        i+=1
        j+=1
    if j==m:
        return 1
    else:
        return 0


T=int(input())
for t in range(1,T+1):
    str1,str2= [input() for _ in range(2)]
    print(f'#{t} {search(str1,str2)}')