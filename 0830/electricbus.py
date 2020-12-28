t=int(input())
for tc in range(1,t+1):
    k,m,n=map(int,input().split())
    bus_station=list(map(int,input().split()))
    cnt=0
    st=0
    st+=k
    for i in range(n-1):
        if k < bus_station[i + 1]-bus_station[i]:
            cnt = 0
            print(f'#{tc} {0}')
            break

    for i in range(m):
        if st in bus_station:
            if st>=m:
                break
            st+=k
            cnt+=1
            continue
        else:
            if st>=m:
                break
            st-=1

    if st>=m: # 위에 방지
        print(f'#{tc} {cnt}')

'''
1
3 10 5
1 3 5 7 9
'''