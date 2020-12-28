import sys
sys.stdin=open("node_input.txt","r")

def check_node(n,length):
    visited=[n]
    q=[]
    q.append((n,length))
    while q:
        v,length=q.pop(0)
        result.append([v,length])
        for w in range(101):
            if matrix[v][w]==1 and not w in visited:
                q.append((w,length+1))
                visited.append(w)
    return result

for tc in range(1,11):
    data_l,start_n= map(int,input().split())
    nodes=list(map(int,input().split()))
    matrix=[[0]*101 for _ in range(101)]
    end_length=0
    max_node=0
    result=[]
    for k in range(data_l//2):
        s,e=nodes[k*2],nodes[(k*2)+1]
        matrix[s][e]=1
    check_node(start_n,0)

    for k in result:
        if k[1]>=end_length:
            end_length=k[1]

    for k in result:
        if k[1]==end_length:
            if k[0]>max_node:
                max_node=k[0]

    print(f'#{tc} {max_node}')

'''
300 55
55 12 42 76 60 26 22 71 27 35 6 84 51 99 80 2 94 35 38 35 57 94 77 6 63 49 82 1 14 42 56 56 43 63 12 78 25 79 53 44 97 74 41 14 76 73 19 11 18 33 13 96 70 32 41 89 86 91 98 90 91 46 54 15 52 41 45 59 36 60 93 6 65 82 4 30 76 9 93 98 50 57 62 28 68 42 30 41 14 75 2 78 16 84 14 93 25 2 93 60 71 29 28 85 76 87 99 71 88 48 5 4 22 64 7 64 11 72 90 41 65 43 20 14 92 5 19 33 51 6 76 40 4 23 99 48 85 49 72 65 14 76 46 13 47 79 70 63 20 86 90 45 66 41 46 9 19 71 2 24 33 73 53 88 71 64 2 4 24 28 1 70 16 66 29 44 48 89 44 38 10 64 50 82 89 43 9 61 22 59 55 89 47 91 50 44 31 21 49 68 37 84 36 27 86 39 54 30 25 49 24 60 58 67 45 56 19 27 12 26 56 2 50 97 85 16 65 43 76 14 43 97 49 73 27 7 74 30 5 6 27 13 76 94 66 37 37 42 15 95 57 53 37 39 83 56 16 32 31 42 26 12 38 87 91 51 63 35 94 54 17 53 9 63 34 55 4 35 4 57 49 25 18 14 10 29 1 81 19 59 51 56 62 65 4 77 44 10 3 62 
'''