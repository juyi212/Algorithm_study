import math

pocket = [(0, 0), (127, 127), (127, 254), (0, 127), (0, 254), (127, 0)]

# 흰공 위치
start = (126, 15)

# 목표공 위치
ball = (122, 8)

for i in range(1):
    cos_xy = ball[0] / (math.sqrt((ball[0] - pocket[i][0]) ** 2 + (ball[1] - pocket[i][1]) ** 2))
    sin_xy = ball[1] / (math.sqrt((ball[0] - pocket[i][0]) ** 2 + (ball[1] - pocket[i][1]) ** 2))
    tmpcos = math.acos(cos_xy) #역함수 이용, 비율을 라디안 각으로 나오게함
    tmpsin = math.acos(sin_xy)
    # print(tmpcos)
    # print(tmpsin)
    degree = tmpcos * 180 / math.pi # 각도로 만들어주는 과정

    print(degree)
    x = cos_xy * (math.sqrt((ball[0] - pocket[i][0]) ** 2 + (ball[1] - pocket[i][1]) ** 2) + 5.72)
    y = sin_xy * (math.sqrt((ball[0] - pocket[i][0]) ** 2 + (ball[1] - pocket[i][1]) ** 2) + 5.72)

    # 흰공이 여기로 와야 목표공을 (0,0)으로 쏘아보냄.
    # pocket 6개를 다 생각해보면 됨.
    # 목표공과 흰공 사이에 중간 공이 있다면 옆에 튕겨서 쏘아 보내야 함.
    print(x, y)