n=int(input()) #참외갯수

distance=[list(map(int,input().split()))[1] for _ in range(6)]
print(distance)
max_a=distance.index(max(distance))
max_b=distance.index(max(distance[max_a-1],distance[(max_a+1)%6]))
min_a=(max_a+3)%6
min_b=(max_b+3)%6
r=distance[max_a]*distance[max_b]
c=distance[min_a]*distance[min_b]
print((r-c)*n)

'''
7
3 20
1 100
4 50
2 160
3 30
1 60
'''