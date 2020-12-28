# 상자로 채워진 방이있다.
# 90도 회전이 끝난 이후
# 가장 큰 낙차를 구하면 된다.
# 오른쪽에 무엇이 있냐 (오른쪽으로 회전이기때문에)

#각 줄의 가장 높이 있는 상자의 낙차가 각줄에서 가장 크다.
#낙차를 구하는 방법:
# 현재 오른쪽에 비어있거나 높이가 자신보다 작은 상자이면, 낙차를 하나씩 더하면 된다.

#모든 열의 낙차를 구하고, 그 중에서 가장 큰 낙차를 반환
# 하나의 열의 낙차부터 구하기

boxes=[7,4,2,0,0,6,0,7,0]
#step 1 : 가장 왼쪽에 있는 열(0번)의 낙차 구하기

# target=boxes[0]
# for i in range(1,len(boxes)+1): #1번열부터 끝까지 순회
#     if boxes[i]<target:
#         cnt+=1
# print(cnt)

#step 2 : 모든 열의 낙차를 구하고 최고 낙차 구하기

max_cnt=0
for i in range(0,len(boxes)):
    target = boxes[i]
    cnt=0
    for j in range(i+1,len(boxes)):
        if boxes[j] < target:
            cnt+=1
    print(cnt)
    if cnt>max_cnt:
        max_cnt=cnt
print(max_cnt)