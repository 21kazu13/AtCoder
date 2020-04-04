def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

D = iil()
J = iil()
ans = 0
for x,y in zip(D,J):
    ans += max(x,y)
print(ans)