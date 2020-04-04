def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
X = iil()
ti = 100*100*100
for i in range(1,101):
    cal = 0
    for item in X:
        cal += (item-i)**2
    ti = min(cal,ti)

print(ti)