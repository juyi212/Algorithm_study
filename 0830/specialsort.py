t=int(input())
for tc in range(1,t+1):
    n=int(input())
    numbers=list(map(int,input().split()))
    numbers.sort()
    print(numbers)
    result=[0]*n
    for i in range(0,10,2):
        result[i]=numbers[-1]
        numbers.pop()
    for j in range(1,10,2):
        result[j]=numbers[0]
        numbers.pop(0)
    print(result)