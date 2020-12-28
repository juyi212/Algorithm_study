def roll(idx, clock):

    if clock == 1:
        tmp = zigs[idx].pop()
        zigs[idx].insert(0, tmp)

    else:
        tmp = zigs[idx].pop(0)
        zigs[idx].append(tmp)

#자석이 영향을 받아서 돌아가는지 확인하는 함수
#만약에 영향을 받아서 돌아가는 자석이라면, 돌리면됨
#dix : 확인할 자석의 인덱스
# dir : 검사를 진행하고있는 방향(왼쪽, 오른쪽) 1.왼쪽탐색, 2.오른쪽탐색, 3. 시장
#clock : 회전방향
def check(idx, clock, dir):
    if idx < 0 or idx >= 4:
        return
    if dir == 3:
        #   왼쪽검사실행
        check(idx-1, -clock, 1)
        #   오른쪽검사실행
        check(idx + 1, -clock, 2)
        roll(idx, clock)
    elif dir == 1:
        # 왼쪽으로 진행중이었는가
        if zigs[idx][2] != zigs[idx+1][6]:
            check(idx - 1, -clock, 1)
            roll(idx, clock)
    elif dir == 2:
        #   오른쪽으로 진행중이었는가
        if zigs[idx][6] != zigs[idx-1][2]:
            check(idx + 1, -clock, 2)
            roll(idx, clock)


for tc in range(1,int(input())+1):
    N = int(input())
    zigs = [list(map(int,input().split())) for _ in range(4)]

    for i in range(N):
        idx, clock = map(int, input().split())
        #해당인덱스에 있는 자석을 돌린다
        #어떤자석이 돌아갈지 검사
        check(idx-1, clock, 3)
    result = 0
    for i in range(4):
        if zigs[i][0] == 1:
            result += i**2
    print(result)