arr=[
    [1,2,3],
     [4,5,6]
     ,[7,8,9]
     ]
#행우선
n=len(arr) #행의 길이
m=len(arr[0]) #열의 길이
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
print()

for j in range(m): #열
    for i in range(n):
        print(arr[i][j],end=" ")
    print()
print()