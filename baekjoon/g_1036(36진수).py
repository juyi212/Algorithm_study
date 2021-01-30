
n = int(input())
value = [0] * 36
for i in range(n):
    word = input()
    cnt = 0
    for j in range(len(word)-1, -1, -1):
        value[int(word[j], 36)] += 36 ** cnt
        cnt += 1

k = int(input())
a = [[value[i]*(35-i), i] for i in range(36)]   # Z 로 바꿨을때 더해지는 실제값, 가중치
a.sort(reverse=True)
chg_num = []

for i in range(k):
    chg_num.append(a[i][1]) # 바꿔줘야할 인덱스 값을 저장. 즉 문자
number_chg = [0] * 36

for i in range(36):
    if i in chg_num:
        number_chg[i] = 35 * value[i] # z 값으로 바꿔주고 넣어줌
    else:
        number_chg[i] = i * value[i]

total = sum(number_chg)
result = ''

while total:
    a = total % 36
    if 0 <= a <= 9:
        result = chr(48 + a) + result
    else:
        result = chr(55 + a) + result   # 10부터 알파벳이기때문에 65에서 10을 빼줌
    total = total // 36

if not result:
    print(0)
else:
    print(result)

'''
3
0
0
0
0

'''


'''
16242413

13 * 1
24 * 36**1
24 * 36**2

'''
''''
5
GOOD
LUCK
AND
HAVE
FUN
7
'''