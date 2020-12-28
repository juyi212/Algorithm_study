import sys
sys.stdin=open("sample_input_special.txt","r")

def selectionsort(a):
    total =[0] * 10
    for i in range(0,len(a)-1):
        min=i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                min=j
        a[i],a[min] = a[min],a[i]
    x=[]
    y=[]
    print(a)
    for j in range(len(a)-1,len(a)-6,-1):
        x.append(a[j])

    for j in range(0,5):
        y.append(a[j])
    for max_v in range(0,len(total),2):
        total[max_v]=x[0]
        x.remove(total[max_v])

    for min_v in range(1,len(total),2):
        total[min_v] = y[0]
        y.remove(total[min_v])

    return total

T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    n=list(map(int,input().split()))
    print(f'#{test_case}',end=" ")
    result = selectionsort(n)
    for i in result:
        print(i,end=" ")
    print()

