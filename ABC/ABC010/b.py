def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()
l = [3,0,1,0,1,2]
ans = 0
for i in A:
    ans += l[i%6]
print(ans)