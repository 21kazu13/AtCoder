def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
s,t = ism()
ans = ''
for i in range(n):
    ans += (s[i]+t[i])
print(ans)