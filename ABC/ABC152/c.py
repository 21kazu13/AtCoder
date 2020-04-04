def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
P = iil()
mP = P[0]
ans = 0
for i in range(n):
    if mP >= P[i]:
        ans += 1
    mP = min(mP,P[i])

print(ans)