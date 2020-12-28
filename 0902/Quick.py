# 퀵 정렬
# 피벗을 정하고 피벗보다 작은 값들을 앞쪽으로
# 피벗보다 큰 값을 뒤쪽으로 보내면, 피벗의 위치가 결정된다.
# 나누어진 부분을 다시 피벗을 기준으로 정리하면 계속해서 피벗의 위치가 결정되기때문에
# 끝까지 진행하면 , 정렬이 완료된다.

# 퀵정렬의 두 가지 작업
# 파티션 : 전체를 두 부분으로 나누는 작업
# 퀵정렬 : 나누어진 두 부분을 각각 다시 퀵정렬

def partition(arr,start,end):
    # 피벗 선택하고, 제일 앞쪽 값을 피벗으로 설정(피벗은 달라질 수 있다.)
    pivot=arr[start]
    # 피벗보다 작으면 앞쪽으로, 크면 뒤쪽으로 보내기
    left=start+1 # 피벗은 검사할 필요 없음
    right=end

    while left <= right: # left가 right보다 커지면 종료
    # left가 오른쪽으로 이동하며, 피벗보다 큰 값을 찾기
        while left<= right and arr[left]<=pivot:
            left+=1
        # right가 왼쪽으로 이동하며, 피벗보다 작은 값 찾기
        while left<=right and arr[right]>=pivot:
            right-=1
        # 각각 큰값과 작은 값을 찾앗으면, 위치 교환
        if left<right:
            arr[left],arr[right]=arr[right],arr[left]
    #피벗을 제외하고, 피벗보다 작으면 왼쪽,피벗보다 크면 오른쪽에 위치 시키기
    #피벗이 중간자리에 위치하게 됨.
    arr[start],arr[right]=arr[right],arr[start]

    return right #피벗위치 반환

def quick_sort(arr,start,end):
    if start<end:
        # 파티션을 실행하고, 파티션으로 나누어진 부분을 각각 다시 퀵 소트
        pivot=partition(arr,start,end) # 인덱스가 결정된 상태임

        quick_sort(arr, start, pivot-1)
        quick_sort(arr,pivot+1,end)
    else:
        return # 주석 처리해도됨.


target=[3,5,1,2,7,4,6]
quick_sort(target,len(target)-1)
print(target)

