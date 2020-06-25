def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

from collections import Counter

n = ii()
A = iil()
s = sum(A)
d = Counter(A)

q = ii()

for i in range(q):
    b,c = iim()
    m = d.pop(b,0)
    if m:
        d[c] = d.get(c,0)+m
    s += (c-b)*m
    print(s)
