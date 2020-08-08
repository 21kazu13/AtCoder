def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
from collections import Counter

n = ii()
s = input()

d = Counter(s)
num = d['R']
ans = num
wcnt = 0
rcnt = 0
for i in s:
#    print(i)
    if i == 'W':
        wcnt += 1
    else:
        if num - 1 >= wcnt or wcnt == 0:
            ans -= 1
            num -= wcnt+1
            wcnt = 0
        if num == 0:
            break
print(ans)