import sys

N, K = map(int, sys.stdin.readline().split()) # 멀티탭 구멍 수, 전기용품 사용횟수
uses = list(map(int, sys.stdin.readline().rsplit()))

multitab = []

cnt = 0

for idx in range(len(uses)):
    if len(multitab) < N:
        # multitab 이 다 채워진후
        if uses[idx] not in multitab:
            multitab.append(uses[idx])
        else:
            continue
    else:
        # 다음 숫자를 보았을 때 채워져있으면 pass
        if uses[idx] not in multitab:
            # 아니면 채워져있는 숫자 중에서 가장 나중에 바뀌는 숫자 선택하기
            change = 0
            flag = False
            for m in multitab:
                if m not in uses[idx:len(uses)]:
                    cnt += 1
                    multitab.remove(m)
                    flag = True
                    multitab.append(uses[idx])
                    break
                ch = uses.index(m,idx,len(uses))
                change = max(change, ch)
            if not flag:
                value = uses[change]
                multitab.remove(value)
                cnt += 1
                multitab.append(uses[idx])
print(cnt)

