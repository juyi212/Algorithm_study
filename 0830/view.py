for tc in range(1,11):
    n=int(input())
    home=list(map(int,input().split()))
    count=0
    for i in range(len(home)-4):
        slice=home[i:i+5]
        if max(slice)!=slice[2]:
            continue
        else:
            slice.sort()
            count+=slice[-1]-slice[-2]
    print(count)
