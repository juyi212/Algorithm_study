import collections

def bfs():
    q=collections.deque()
    q.append((num,0))
    while q:
        st,cnt=q.popleft()
        if st == target:
            return cnt
        for i in range(N-K+1):
            new=st[:]
            new[i:i+K]=new[i:i+K][::-1] # 바로 넣기 가능

            s_new=''.join(new)

            if not s_new in visit:
                visit.add(s_new)
                q.append((new, cnt + 1))
    return -1

N,K=map(int,input().split()) #n 순열의 크기 , k 뒤집을 개수
num=input().split()
target=sorted(num) #sorted 는 iterable한 자료형에서는 다 작동한다.
visit=set()
print(bfs())