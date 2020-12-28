def check():
    ans=0
    for i in range(n):
        cnt=0
        for j in range(n):
            if words[i][j]=='0':# 11101 방지
                if cnt==k:
                    ans+=1
                cnt=0
                continue
            cnt+=1
        if cnt==k: # 11110 방지
            ans+=1

    for i in range(n):
        cnt=0
        for j in range(n):
            if words[j][i]=='0':
                if cnt==k:
                    ans+=1
                cnt=0
                continue
            cnt+=1
        if cnt==k:
            ans+=1
    return ans

T=int(input())
for tc in range(1,T+1):
    n,k =map(int,input().split())
    words=[input().split() for _ in range(n)]
    print(f'#{tc} {check()}')

'''
1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0 
'''