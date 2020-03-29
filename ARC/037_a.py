def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
l = iil()

ans = 0
for item in l:
    if item < 80:
        ans += 80-item
print(ans)