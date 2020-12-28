import sys
sys.stdin=open('sample_input_card.txt','r')

def Max(li2):
    max_num=li[0]
    for num in li2:
        if max_num<num:
            max_num=num
    return max_num

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = input()
    li=[]
    dic={}
    for i in a:
        li+=[int(i)]
    for j in li:
        if j in dic:
            dic[j]+=1
        else:
            dic[j]=1
    max_v =0
    max_k =1
    for z in range(0,10):
        if z not in dic:
            continue
        if dic[z] > max_v:
            max_v=dic[z]
            max_k=z
        elif dic[z] == max_v: # value 값들이 같을 때
            if max_k < z:
                max_k = z

    print(f'#{test_case} {max_k} {max_v}')





