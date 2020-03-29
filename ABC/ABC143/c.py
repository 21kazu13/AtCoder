def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
s = list(input())
ans = 1
for i in range(1,n):
    if s[i] != s[i-1]:
        ans += 1
print(ans)