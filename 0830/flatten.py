for tc in range(1,11):
    dump=int(input())
    boxes=list(map(int,input().split()))
    while dump>0:
        m=boxes.index(max(boxes))
        n=boxes.index(min(boxes))
        boxes[m]=boxes[m]-1
        boxes[n]=boxes[n]+1
        dump-=1
    print(f'{tc} {max(boxes)-min(boxes)}')