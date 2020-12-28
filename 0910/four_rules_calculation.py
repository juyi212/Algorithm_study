#이진트리로 표현되었다는 것은 연산자규칙에 맞게 표기 되어있다는 것임.
#단말노드- 피연산자, 내부노드-연산자

def check(node):
    if node: #후위
        check(tree[node][1])
        check(tree[node][2])
        s.append(tree[node][0])
    return s
for tc in range(1,11):
    N=int(input())
    tree = [[0]*3 for _ in range(N + 1)]
    s=[]
    for i in range(1,N+1): #idx가 노드 번호
        info = input().split()
        tree[i][0]= info[1] if info[1] in ['+','-','*','/'] else int(info[1]) #피연산자, 연산자, 연산자
        if len(info)>3:
            tree[i][1]= int(info[2])
            tree[i][2] =int(info[3])
    check(1)
    stack=[]

    for i in s:
        if i=='-':
            num2=stack.pop()
            num1=stack.pop()
            stack.append(int(num1)-int(num2))
        elif i=='+':
            num2=stack.pop()
            num1=stack.pop()
            stack.append(int(num1)+int(num2))
        elif i=='*':
            num2=stack.pop()
            num1=stack.pop()
            stack.append(int(num1)*int(num2))
        elif i=='/':
            num2=stack.pop()
            num1=stack.pop()
            stack.append(int(num1)/int(num2))
        else:
            stack.append(i) #피연산자 저장

    if len(stack)==1:
        a=stack.pop()
        print(f'#{tc} {int(a)}')


'''
107
1 * 2 3
2 * 6 7
3 / 4 5
4 + 8 9
5 * 10 11
6 / 12 13
7 / 14 15
8 * 16 17
9 - 18 19
10 - 20 21
11 / 22 23
12 + 24 25
13 / 26 27
14 - 28 29
15 / 30 31
16 - 32 33
17 / 34 35
18 - 36 37
19 + 38 39
20 * 40 41
21 / 42 43
22 + 44 45
23 / 46 47
24 / 48 49
25 - 50 51
26 * 52 53
27 + 54 55
28 / 56 57
29 + 60 61
30 - 62 63
31 / 58 59
32 - 64 65
33 - 66 67
34 * 68 69
35 / 70 71
36 + 72 73
37 / 74 75
38 + 76 77
39 / 78 79
40 - 80 81
41 - 82 83
42 + 84 85
43 / 86 87
44 + 88 89
45 - 90 91
46 * 92 93
47 / 94 95
48 * 96 97
49 + 98 99
50 - 100 101
51 * 102 103
52 / 104 105
53 2
54 3
55 1
56 * 106 107
57 8
58 7
59 7
60 13
61 20
62 78
63 68
64 102
65 80
66 29
67 12
68 10
69 2
70 100
71 10
72 44
73 97
74 60
75 1
76 13
77 20
78 248
79 8
80 94
81 89
82 49
83 47
84 18
85 52
86 20
87 2
88 1
89 2
90 113
91 95
92 7
93 7
94 28
95 4
96 30
97 2
98 4
99 1
100 284
101 85
102 3
103 2
104 70
105 7
106 252
107 2
'''