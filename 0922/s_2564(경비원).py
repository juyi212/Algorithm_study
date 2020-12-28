def check(x,y):
    if x==1:
        return y
    elif x==2:
        return width+height+(width-y)
    elif x==3:
        return width+height+width+(height-y)
    elif x==4:
        return width+y

width,height=map(int,input().split())
n=int(input()) #가게 수
stores=[list(map(int,input().split())) for _ in range(n)]
dg_dir,dg_len=map(int,input().split())
dg=check(dg_dir,dg_len)
result=0

for i in range(len(stores)):
    s_dir,s_len=stores[i][0],stores[i][1]
    len=check(s_dir,s_len)
    result+=min(abs(dg-len),(height+width)*2-abs(dg-len))

print(result)




'''
10 5
3
1 4
3 2
2 8
2 3
'''