import sys
sys.stdin = open("sample_input.txt", "r")

def hi(li,r,c):
    for i in range(r):
        if li[i] == li[i][::-1]:  # row
            return f'#{tc} {li[i]}'

    col_li = []
    for i in range(r):
        col=''
        for j in range(r):
            col+=li[j][i]
        col_li.append(col)

    for i in range(r):
        if col_li[i] == col_li[i][::-1]:
            return f'#{tc} {col_li[i]}'

    for i in range(r):
        for j in range((r-c)+1):
            new=''
            for z in range(j,j+c):
                new+=li[i][z]
            if new == new[::-1]:
                return f'#{tc} {new}'

    for i in range(r):
        for j in range((r - c) + 1):
            c_new = ''
            for z in range(j, j + c):
                c_new += col_li[i][z]
            if c_new == c_new[::-1]:
                return f'#{tc} {c_new}'

T=int(input())
for tc in range(1,T+1):
    r,c=map(int,input().split())
    li=[input() for _ in range(r)]
    print(hi(li,r,c))

