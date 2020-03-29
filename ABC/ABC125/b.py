def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
v = iil()
c = iil()
cal = zip(v,c)
ans = 0
for i in cal:
    ans += max(0,i[0]-i[1])
print(ans)