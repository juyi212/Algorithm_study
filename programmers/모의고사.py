def solution(answers):
    one = [1, 2, 3, 4, 5]  # 5
    two = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    person = [0, 0, 0]
    for idx, value in enumerate(answers):
        o = idx % 5
        tw = idx % 8
        th = idx % 10
        if value == one[o]:
            person[0] += 1
        if value == two[tw]:
            person[1] += 1
        if value == three[th]:
            person[2] += 1

    max_v = max(person)
    here = []
    for i in range(len(person)):
        if max_v == person[i]:
            here.append(i+1)

    return here

