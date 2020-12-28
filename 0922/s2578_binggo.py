import sys
def isBingo():

    res = 0
    # 가로 확인
    for i in range(5):
        flag = True
        if 0 in check[i]:
            flag = False
        if flag:
            res += 1

    # 세로 확인
    check_T = list(map(list,zip(*check)))
    for i in range(5):
        flag = True
        if 0 in check_T[i]:
            flag = False
        if flag:
            res += 1


    # 대각선
    r_flag, l_flag = True, True
    for i in range(5):
        if check[i][i] == 0:
            r_flag = False
        if check[i][4-i] == 0:
            l_flag = False
    if r_flag:
        res += 1
    if l_flag:
        res += 1

    if res >= 3:
        return True
    return False


bingo = list()
numbers = list()
check = [[0] * 5 for _ in range(5)]
count = 0

for _ in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))
for _ in range(5):
    numbers.append(list(map(int, sys.stdin.readline().split())))

for number in numbers:
    while number:
        num = number.pop(0)
        count += 1

        for i in range(5):
            for j in range(5):
                if bingo[i][j] == num:
                    check[i][j] = 1
                    i = 5
                    break

        if count >= 5:
            if isBingo() == True:
                print(count)
                exit()

# def check1():
#     total=0
#
#     for i in range(5):
#         f=True
#         if 0 in check[i]:
#             f=False
#         if f:
#             total+=1
#
#     t_check = list(map(list, zip(*check)))
#     for i in range(5):
#         f=True
#         if 0 in t_check[i]:
#             f=False
#         if f:
#             total+=1
#
#
#     r,c=True,True
#     for i in range(5):
#         if check[i][i]!=0:
#             r=False
#         if check[i][4-i]!=0:
#             c=False
#     if r:
#         total+=1
#     if c:
#         total+=1
#
#     if total>=3:
#         return True
#     return False
#
#
# binggo=[list(map(int,input().split())) for _ in range(5)]
# teacher=[list(map(int,input().split())) for _ in range(5)]
# check = [[0] * 5 for _ in range(5)]
# cnt=0
#
# for i in teacher:
#     while i:
#         num=i.pop(0)
#         cnt+=1
#         for x in range(5):
#             for y in range(5):
#                 if binggo[x][y]==num:
#                     check[x][y]=1
#                     x=5
#                     break
#         if cnt>=5:
#             if check1()==True:
#                 print(cnt)
#                 exit()
