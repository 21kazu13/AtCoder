def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

from collections import Counter

n = ii()
A = iil()
di = Counter(A)
A.sort()

ans = 0
l = set()
for item in A:
    if di[item] > 1:
        if item not in l:
            for i in range(1,1000000//item+1):
                l.add(item*i)
        continue
    if item not in l:
        for i in range(1,1000000//item+1):
            l.add(item*i)
        ans += 1
print(ans)
