def solution(k, room_number):
    # input 값이 1조임
    # 시간초과를 해결하기 위해서는 유니온파인드나 다른 방법들을 써야함

    # 시간초과남
    # rm = [False] * k
    # answer = []
    # for i in room_number:
    #     if rm[i] == False:
    #         answer.append(i)
    #         rm[i] = True
    #     else:
    #         ch = i
    #         while ch <= k:
    #             ch += 1
    #             if rm[ch] == False:
    #                 answer.append(ch)
    #                 rm[ch] = True
    #                 break
    #
    # return answer
    
    def check(number, rooms):
        if number not in rooms:
            rooms[number] = number+1
            return number
        empty = check(rooms[number], rooms)
        rooms[number] = empty+1
        return empty

    rooms = dict()
    for num in room_number:
        ch_room = check(num, rooms)
    return list(rooms.keys())


print(solution(10, [1,3,4,1,3,1]))