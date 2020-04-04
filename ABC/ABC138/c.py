def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
V = sorted(iil())

ans = V[0]

for i in V:
    ans = (ans+i)/2

print(ans)