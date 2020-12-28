def palindrome(n,m):
    result=''
    for i in range(n):
        for j in range((n-m)+1):
            for k in range(m//2):
                if string[i][j+k]!=string[i][j+m-k-1]:
                    break
            else:
                result=string[i][j:j+m]
                return result

    for i in range(n):
        for j in range(n-m+1):
            for k in range(m//2):
                if string[j+k][i]!=string[j+m-k-1][i]:
                    break
            else:
                for x in range(j,j+m):
                    result+=string[x][i]
                return result

t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    string=[input() for _ in range(n)]
    result=palindrome(n,m)
    print(f'#{tc} {result}')