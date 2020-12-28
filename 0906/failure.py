def solution(N, stages):
    ranks=[0]*(N+1) #0,N+1 자리까지

    for i in stages:
        ranks[int(i)-1]+=1
    print(ranks)

    # stages 에서 같은 원소를 찾고 전에 len 길이 에서 나눠주고 지우고..



    answer = []
    return answer



N=5
stages=[2,1,2,6,2,4,3,3]
print(solution(N,stages))


'''
4
stages=[4,4,4,4,4]
'''