def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
import numpy as np

n = ii()
A = iil()

l = np.cumsum(A)
su = l[-1]
#print(l)
ans = 1e18
for i in range(n-1):
    x = l[i]
    y = su - x
    ans = min(ans,abs(x-y))

print(ans)