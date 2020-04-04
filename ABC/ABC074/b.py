def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
k = ii()
x = iil()
ans = 0
for i in x:
    ans += min(i, k-i)
print(ans*2)