
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b = iim()
ans = 0
for i in range(a,b+1):
    s = str(i)
    if s == s[::-1]:
        ans += 1

print(ans)