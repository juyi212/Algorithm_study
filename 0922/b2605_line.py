n=int(input())
number=list(map(int,input().split()))

newline=[]
for i in range(len(number)):
    if i ==0:
        newline.append(i+1)
    else:
        c=number[i]
        if c==0: #뽑은 번호표가 0일때
            newline.append(i+1)
        else:# 아닐때
            newline.insert(i-c,i+1)

print(*newline,end=' ')
