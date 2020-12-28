t=int(input())
for tc in range(1,t+1):
    N=int(input())
    scores=list(map(int,input().split()))

    visit=[0]*(sum(scores)+1)
    result=[0]
    for i in scores:
        for j in range(len(result)):
            if visit[i+result[j]]==0: #방문여부 체크해줘야함
                result.append(i+result[j])
                visit[i+result[j]]=1
    print(f'#{tc} {len(result)}')

    # print(f'#{tc} {visit.count(1)+1}')


    #
    # visit=[0]*(sum(scores)+1)
    # Q=[[0,0]] #k,s
    # while Q:
    #     k,s=Q.pop(0)
    #     if k==N:
    #         print(s,end=' ')
    #         visit[s]=1
    #     else: #중복 제거 해줘야함.
    #         Q.append([k+1,s])
    #         Q.append([k + 1, s+scores[k]])

'''

2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1
'''