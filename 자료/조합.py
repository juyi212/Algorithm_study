arr = ['a','b','c','d','e']
n = len(arr)

# 5C3
for i in range(n-2):    # 3개 뽑기
    for j in range(i+1, n-1):   # 2
        for k in range(j+1, n): # 1
            print(arr[i], arr[j], arr[k])


