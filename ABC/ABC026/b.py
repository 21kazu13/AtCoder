import math
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
R = []
ans = 0
for i in range(n):
    R.append(ii())

R = sorted(R,reverse=True)

for j in range(n):
    if j%2 == 0:
        ans += R[j]**2
    else:
        ans -= R[j]**2
print(ans*math.pi)