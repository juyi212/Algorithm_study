
def solution(s):
    for c in range(len(s), 0, -1):
        # 어차피 자르는걸 맨 마지막부터 하니깐 같으면 바로 출력 ㄱ ㄱ
        for start in range(len(s)):
            cutstr = s[start:start+c]
            if cutstr == cutstr[::-1]:
                return len(cutstr)
            if start + c >= len(s):
                break


print(solution('baaa'))
