from collections import Counter

def solution(participant, completion):
    # answer= Counter(participant) - Counter(completion)
    # return list(answer.keys())[0]

    # sort가 중요 포인트이다...
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    else:
        return participant[-1]


    #   시간을 줄여야 한다...
    # ch = [0] * len(participant)
    # for idx, name in enumerate(participant):
    #     if completion:
    #         if name in completion:
    #             ch[idx] = 1
    #             completion.remove(name)
    #
    # for i in range(len(ch)):
    #     if not ch[i]:
    #         answer = participant[i]
    #         return answer



participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
print(solution(participant, completion))

participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']
print(solution(participant, completion))
