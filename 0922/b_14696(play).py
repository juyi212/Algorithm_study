# 별 동그라미 네모 세모 순

N=int(input())

for i in range(N):
    c1 = []
    c2 = []
    v1,*vv1=map(int,input().split())
    c1+=[*vv1]
    v2,*vv2=map(int,input().split())
    c2+=[*vv2]

    if c1.count(4)!=c2.count(4):
        if c1.count(4)>c2.count(4):
            print('A')
        else:
            print('B')
    else:
        if c1.count(3)!=c2.count(3):
            if c1.count(3)>c2.count(3):
                print('A')
            else:
                print('B')
        else:
            if c1.count(2)!=c2.count(2):
                if c1.count(2) > c2.count(2):
                    print('A')
                else:
                    print('B')
            else:
                if c1.count(1)!=c2.count(1):
                    if c1.count(1) > c2.count(1):
                        print('A')
                    else:
                        print('B')
                else:
                    print('D')