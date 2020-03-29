def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
a,b = iim()

ans = 0

if a>b:
    ans += a
    ans += max(a-1,b)
else:
    ans += b
    ans += max(a,b-1)

print(ans)