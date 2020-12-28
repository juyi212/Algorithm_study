t=int(input())
for tc in range(1,t+1):
    str1=input()
    str2=input()
    i=0
    j=0
    m=len(str1)
    n=len(str2)
    count=0
    while j<n:
        if j ==n:
            break
        if str1[i] ==str2[j]:
            if i == m-1:
                count+=1
                i=0
            i+=1
            j+=1
        else:
            i=0
            j+=1
    print(f'#{tc} {count}')
