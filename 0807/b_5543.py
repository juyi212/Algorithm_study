price=[]
for i in range(5):
    s=int(input())
    price+=[s]


hp=[]
bp=[]
for i in range(3):
    hp.append(price[i])

for j in range(-1,-3,-1):
    bp.append(price[j])

min=hp[0]
result=[]
for i in range(len(hp)):
    for j in range(len(bp)):
        result+=[hp[i]+bp[j]]

result.sort()
print(result[0]-50)

