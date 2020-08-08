def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

import numpy as np

n,m,k = iim()
a = iil()
cuma = [0]
for i in a:
    cuma.append(cuma[-1]+i)
b = iil()
cumb = [0]
for i in b:
    cumb.append(cumb[-1]+i)

best = m
ans = 0
for i in range(n+1):
    if cuma[i] > k:
        break
    while cumb[best] > k-cuma[i]:
        best -= 1
    ans = max(ans,best+i)

print(ans)
