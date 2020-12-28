def seq_search(a,n, key):
    i=0
    while i<n and a[i] != key:
        i+=1 # 같게되면 while 문을 나옴
    if i<n:
        return i
    else: return -1


arr=[4,9,11,23,2,19,7]
key=0
print(seq_search(arr,len(arr),key))

# 정렬이 되어 있는 경우
#arr=[1,2,3,4,5,6,7,8]
# def seq_search(a,n, key):
#     i=0
#     while i<n and a[i] < key:
#         i+=1 # 같게되면 while 문을 나옴
#     if i<n and a[i]==key:
#         return i
#     else: return -1