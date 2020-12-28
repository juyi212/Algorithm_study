from itertools import combinations

a=[int(input()) for _ in range(9)]
dwarf=list(combinations(a,7))
for i in dwarf:
    if sum(i)==100:
        k=sorted(i)
        for j in k:
            print(j)
        break



'''
99
1
99
1
1
1
1
1
94
    
'''