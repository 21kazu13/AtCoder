def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m,c = iim()
B = iil()
ans = 0
for i in range(n):
    A = iil()
    cond = c
    for x,y in zip(A,B):
        cond += x*y
    if cond > 0:
        ans += 1
print(ans)