import sys
sys.stdin = open("s_input.txt", "r")

def circle(li):
    count_li=[]
    for i in range(100):
        count = 0
        for j in range(100): # 고정
            r_new =''
            for z in range(j,100):
                r_new += li[i][z]
                if r_new[0]==r_new[-1]:
                    if r_new == r_new[::-1]:
                        count =len(r_new)
                        count_li.append(count)

    rm_count=max(count_li)
    count_li.clear()
    col_li=[]
    for i in range(100): #세로 기준으로 정렬
        col_new=''
        for j in range(100):
            col_new+=li[j][i]
        col_li.append(col_new)

    total_count=[rm_count, ]
    for i in range(100):
        count = 0
        for j in range(100): # 고정
            c_new =''
            for z in range(j,100):
                c_new += col_li[i][z]
                if c_new[0] == c_new[-1]:
                    if c_new == c_new[::-1]:
                        count =len(c_new)
                        total_count.append(count)
    return max(total_count)

for tc in range(10):
    T=int(input())
    li=list([input() for _ in range(100)])
    print(f'#{T} {circle(li)}')