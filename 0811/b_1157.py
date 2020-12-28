n=input()
a=n.upper()
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

max_k=0
max_v=0
count=0

for i in dic:
    if dic[i]> max_v:
        max_k=i
        max_v=dic[i]

for i in dic.values():
    if i == max_v:
        count+=1
        if count >=2:
            print('?')
            break

if count ==1:
    print(max_k)
