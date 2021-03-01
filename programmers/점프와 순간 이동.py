def solution(n):
    # k칸을 앞으로 점프(k 만큼 건전지 사용량), 현재온거리 * 2 -> 순간 이동
    # 어렵게 생각하지말고 순간이동 곱하기 2!!!! 생각하기
    cnt = 0
    while (n != 1):
        if n % 2 == 1:  # 홀수
            n = n - 1
            cnt += 1
        else:
            n = n // 2

    if cnt > 0:
        return cnt + 1  # 1이되었을 ㄸㅐ 하나 더해줘야함
    else:
        return 1

