def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

l,r = iim()
L = iil()
R = iil()

size = set(L)
ans = 0
for i in size:
    ans += min(L.count(i),R.count(i))

print(ans)