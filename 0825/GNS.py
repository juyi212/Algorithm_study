import sys
sys.stdin = open("GNS_test_input.txt", "r")

def gns_sort(num):
    number={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    for i in range(len(num)-1):
        for j in range(len(num)-1-i):
            if number[num[j]]>number[num[j+1]]:
                num[j],num[j+1]= num[j+1],num[j]
    return num


T= int(input())
for t in range(1,T+1):
    tc,n =input().split()
    num=input().split()
    gns_sort(num)
    print(tc,*num)