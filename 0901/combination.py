n=4
selected=[0]*n
arr=[1,2]
t=2
def comb(selected,idx,cnt):
    #idx: 인덱스, cnt : 현재 부분집합이 포함하는 요소 개수
    #idx가 벗어나거나, 원하는 만큼의 요소를 이미 선택했을 때 더이상 진행할 필요 없음
    if cnt==t: # 필요한 개수만큼 선택함
        print(selected)
        return
    if idx>=n: # 범위 벗어남
        return

    #     print(selected)
    #     # for i in range(n):
    #     #     if selected[i]==1:
    #     #         print(arr[i],end=" ")
    #     # print()
    # 요소의 포함/ 미포함 여부 결정
    if idx!=n-1:
        selected[idx]=1
        comb(selected,idx+1,cnt+1)
    selected[idx]=0
    comb(selected,idx+1,cnt)

comb(selected,0,0)