def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

x = ii()
mon = 100
for i in range(1,10000):
    mon *= 1.01
    mon = int(mon)
    if mon >= x:
        ans = i
        break
print(ans)