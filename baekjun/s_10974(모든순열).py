from itertools import permutations

n=int(input())
number=list(map(str,range(1,n+1)))

a=list(map(' '.join,permutations(number,n)))
for i in a:
    print(i)


# for i in range(1,n+1):
#     number+=[i]
#
# a=list(permutations(number,n))
# for j in a:
#     print(*j)
