def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
H = iil()

now = 0
ans = 0
for item in H:
    if item > now:
        ans += item-now
    now = item

print(ans)