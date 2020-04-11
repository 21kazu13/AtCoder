def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
t,a = iim()
H = iil()
mdif = 10**9
ans = 0
for i,item in enumerate(H):
    tem = t - item*0.006
    if abs(tem - a) < mdif:
        ans = i+1
        mdif = abs(tem - a)
print(ans)