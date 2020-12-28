def aa(words):
    if words == words[::-1]:
        return True

n=int(input())
for test_case in range(n):
    words=list(input())
    if aa(words):
        print('0') 
    else:
        b =len(words)
        i=0
        while i<=b//2: #words list 반만큼 
            f=i # 양쪽
            l=b-i-1
            if words[f] != words[l]:
                v = words.pop(f) # index f 위치의 문자를 지워줌
                q=aa(words) 
                words.insert(f, v) # 다시 words 리스트에 f 위치의 단어를 넣어주고
                words.pop(l) # f 반대편 원소 지워주기
                p=aa(words) 
                if q ==1 or p==1: # 한쪽이 1이면 유사회문
                    print('1')
                    break
                else:
                    print('2') # 아니면 회문 아님.
                    break
            i+=1

