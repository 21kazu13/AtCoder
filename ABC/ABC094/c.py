def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
X = iil()
r = sorted(X)
smed = r[n//2-1]
lmed = r[n//2]

for i in X:
    if i <= smed:
        print(lmed)
    else:
        print(smed)