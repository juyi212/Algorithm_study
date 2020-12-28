# 멱집합: 모든 부분집합 (powerset)
# 조합 : 특정 조건을 만족하는 부분 집합
# 순열 : 요소들의 순서 정렬

n=3
arr=[1,2,3] # [0,0,0] 각 요소가 부분집합에 포함되는지 표시하는 배열
selected=[0]*3


#idx 몇 번째 요소의 포함여부를 결정할지 표시하는 변수
def powerset(idx):
    if idx==n:
        print(selected)
        for i in range(n):
            if selected[i]==1:
                print(arr[i],end=' ')
        print()
        return
    # 현재 상태에서 실행할 수 있는 모든 경우의 수 실행
    # 현재 요소 포함
    selected[idx]=1
    powerset(idx+1)
    # 현재 요소 미포함
    selected[idx]=0
    powerset(idx+1)
powerset(0)
#부분집합의 합이 5이하인 부분집합을 모두 출력하라