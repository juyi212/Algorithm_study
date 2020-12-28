def selectionsort(a):
    for i in range(0,len(a)-1):
        min = i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
        a[i], a[min] = a[min],a[i] #swap

#k번째로 작은 것
# def selectionsort(a,k):
#     for i in range(k):
#         min = i
#         for j in range(i+1,len(a)):
#             if a[min]>a[j]:
#                 min = j
#         a[i], a[min] = a[min],a[j] #swap
#     return a[k-1]