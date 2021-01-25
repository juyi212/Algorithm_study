def solution(new_id):
    # 소문자 치환
    new_id = new_id.lower()
    # 알파벳 소문자, 숫자, -, _, . 을 제외한 모든 문자 제거
    newnew_id = ''
    for i in new_id:
        if 'a' <= i <= 'z' or '0' <= i <= '9' or i in ["-", "_", "."]:
            newnew_id += i

    # .. -> .
    while True:
        if ".." in newnew_id:
            newnew_id = newnew_id.replace("..",".")
        else:
            break
    # new_id_passed_2 = ''
    # dot_started = False
    # for l in newnew_id:
    #     if l == ".":
    #         if not dot_started:
    #             dot_started = True
    #             new_id_passed_2 += l
    #     else:
    #         dot_started = False
    #         new_id_passed_2 += l
    # newnew_id = new_id_passed_2.strip(".")

    # while i < len(newnew_id):
    #     if newnew_id[i] == '.':
    #         ch += '.'
    #         if i+1 < len(newnew_id):
    #             if newnew_id[i+1] != '.':
    #                 newnew_id = newnew_id.replace(ch, '.')
    #                 ch = ''
    #     i += 1

    # . 처음이나 끝에 위치하면 제거
    if newnew_id:
        if newnew_id[0] == '.':
            newnew_id = newnew_id[1:]
        if newnew_id:
            if newnew_id[-1] == '.':
                newnew_id = newnew_id[:-2]
        # 빈 문자열이라면 a 대입
    if not newnew_id:
        newnew_id = 'a'
        # 16자 이상이면 처음에서 15자까지만 남겨둔다 마지막에 . 위치하면 제거
    if len(newnew_id) > 15:
        newnew_id = newnew_id[:15]
        if newnew_id[-1] == '.':
            newnew_id = newnew_id[:-1]
    # 문자 길이 2이하면 마지막 문자를 3이 될때까지 붙인다.
    elif len(newnew_id) <= 2:
        while len(newnew_id) != 3:
            newnew_id += newnew_id[-1]

    print(newnew_id)


new_id = "...!@BaT#*..y.abcdefghijklm"
solution(new_id)
