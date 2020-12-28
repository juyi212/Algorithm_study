import sys
sys.stdin = open("GNS_test_input.txt", "r")

lis = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for t in range(1,T+1):
    tt, N = input().split()
    string = input()
    print(tt)
    for li in lis:
        print((li+' ')*string.count(li))


# T=int(input())
# for testcase in range(T+1):
#     tn,n =input.split()
#     li=input()

#     a=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     for i in li:


