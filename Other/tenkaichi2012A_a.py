def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
a = [1,1]
if n > 1:
    for i in range(n):
        a.append(a[-1]+a[-2])
print(a[n])
