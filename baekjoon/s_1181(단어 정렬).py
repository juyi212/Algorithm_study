words = []
for _ in range(int(input())):
    word = input()
    l = len(word)
    words.append((word, l))

words = list(set(words)) # set 으로 만들기위해 () 이형태로 좌표를 넣어주고
# 중복 없애기 위해 set -> 다음 list

words.sort(key= lambda x: (x[1], x[0])) # 길이, 단어 순

for w in words:
    print(w[0])



