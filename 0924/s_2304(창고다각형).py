n=int(input())
pillar=[]
for i in range(n):
    x,y=map(int,input().split())
    pillar.append((x,y))

pillar.sort() #가장 앞에 있는 값을 기준으로 정렬한다.
roof=[0]*(pillar[-1][0]+1)

for l,h in pillar:
    roof[l]=h

max_idx=roof.index(max(roof))
height=0
for right in range(max_idx):
    if height<roof[right]:
        height=roof[right]
    else:
        roof[right]=height

height=0
for left in range(len(roof)-1,max_idx,-1):
    if height<roof[left]:
        height=roof[left]
    else:
        roof[left]=height

print(sum(roof))



