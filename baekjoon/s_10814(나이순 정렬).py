import sys

n = int(sys.stdin.readline())
peoples = {}
for _ in range(n):
    age, name = input().split()
    peoples[name] = age

# dictionary 도 sorted key나 items 값으로 가능
peoples = sorted(peoples.items(), key=lambda x:x[1])

# import sys
# n = int(sys.stdin.readline())
# member = []
# for i in range(n):
#     member.append(list(sys.stdin.readline().split()))
# member.sort(key=lambda x: int(x[0]))
# for i in range(n):
#     print(member[i][0], member[i][1])