import sys

t=int(sys.stdin.readline())

ip=[list(map(int,sys.stdin.readline().split('.'))) for _ in range(t)]
b_li=[]
for i in ip:
    diff=''
    for j in i:
        f=format(j,'b')
        if len(f)<8:
            bb=f.zfill(8) #8자리로 맞춰주기
            diff+=bb
        else:
            diff+= f
    b_li+=[diff]

i=0
subnet=['0']*32
ip=['0']*32
while i<32:
    b = []
    for j in range(t):
        b+=[b_li[j][i]]
    if len(b)==t:
        s=b.count(b[0])
        if s!=t:
            m=i
            break
        else:
            ip[i]=b[0]
    i+=1

if i==32: #t=1이거나 ip주소가 같을 때를 방지
    m=32
for i in range(m):
    subnet[i]='1'

ans_sub=[]
ans_ip=[]
for i in range(0,len(subnet),8):
    sub=''
    ipip=''
    for j in range(8):
        sub+=subnet[i+j]
        ipip+=ip[i+j]
    ff=int(sub,2)
    pp=int(ipip,2)
    ans_sub+=[ff]
    ans_ip+=[pp]

print('.'.join(map(str,ans_ip)))
print('.'.join(map(str,ans_sub)))




    # 각각의 바이트를 검색해주고 같다면 패스, 다르면 들어가서 탐색
    # m의 자리를 찾기위해 맨 처음 다른 바이트 안에 들어가 이진수로 바꿔주고
    # 이진수로 바꿔준 각 자리를 탐색해서 같으면 패스, 다르면 다른자리 앞이 m이 된다.
    # m의 자리는 0으로 주워져있음
    # m 다음에 오는 자리수에서 경우의 수가 나오고 이 경우의 수에서 가장 작은 값을 출력
    #(만약 다른 바이트가 2개면 최소를 구하기위해서는 처음 말고 두번째 바이트는 0이 될수도있는건가?)
    # 네트워크 마스크는 m의 자리 다음부터 0 (256.256.256.248)
