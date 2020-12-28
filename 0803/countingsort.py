def CountingSort(A,B,k):
    C=[0]*k
    for i in range(0,len(B)):
        C[A[i]] += 1#카운팅

    for i in range(1,len(C)):
        C[i] += C[i-1] #누적

    for i in range(len(B)-1,-1,-1): #7 6 5 4 3 2 1 0
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    #소트 저장

#정수로 표현될 수 있는 자료 (문자, 소수점이 정해져 있는 것들)



a=[0,4,1,3,1,2,4,1] # 소스
b=[0]*len(a) #결과가 저장되는 배열

CountingSort(a,b,10) #10은 최대값
print(a)
print(b)

