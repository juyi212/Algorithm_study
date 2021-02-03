def solution(info, query):
    # 효율성 통과 x
    q_check = [0] * len(query)
    q_ch = []
    for q in range(len(query)):
        lang, job, career, temp = query[q].split(' and ')
        soulfood, score = temp.split()
        score = int(score)
        q_ch.append([lang, job, career, soulfood, score])


    for i in range(len(info)):
        l, j, c, food, sc = info[i].split()
        sc = int(sc)
        cnt = 0
        for q in range(len(q_ch)):
            cnt = 0
            if l != q_ch[q][0] and q_ch[q][0] != '-':
                continue
            if j != q_ch[q][1] and q_ch[q][1] != '-':
                continue
            if c != q_ch[q][2] and q_ch[q][2] != '-':
                continue
            if food != q_ch[q][3] and q_ch[q][3] != '-':
                continue
            else:
                if sc >= q_ch[q][4]:
                    cnt += 1
                    q_check[q] += 1
                    cnt = 0

    print(q_check)









info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query= ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)