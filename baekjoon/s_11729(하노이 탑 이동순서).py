def hanoi(n, start, end, middle, answer):
    if n == 1:
        return answer.append([start, end])
    hanoi(n-1, start, middle, end, answer)
    answer.append([start, end])
    hanoi(n-1, middle, end, start, answer)

answer = []
n = int(input())
hanoi(n, 1, 3, 2, answer)

print(len(answer))
for ans in answer:
    print(ans[0], end =' ')
    print(ans[1])