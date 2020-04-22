def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
s = list(input())
ans = 0
for i in range(1,n):
    be = set(s[:i])
    en = set(s[i:])
    ans = max(ans,len(be&en))

print(ans)