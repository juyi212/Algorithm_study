def dfs(cnt, start, total, again):
    global max_s

    if cnt == M:
        if total > max_s:
            max_s = total
    if again >= 2:
        return
    if start > N:
        return

    dfs(cnt + 1, start + 1, total + matrix[start], 0)   # 밟음
    dfs(cnt, start + 1, total, 1)   # 안밟음 again 으로 체크체크


T = int(input())  # 테스트 케이스 개수를 입력 받음
for tc in range(T):  # 테스트 케이스 개수만큼 반복
    result = 0  # 결과값을 저장하기 위한 변수를 0으로 초기화
    N, M = map(int, input().split())
    matrix = [0] + list(map(int, input().split()))
    max_s = -1
    dfs(0, 1, 0, 0)
    print(max_s)
