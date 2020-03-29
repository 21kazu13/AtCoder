def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
a,d = iim()

if d > a:
    print((a+1)*d)
else:
    print((d+1)*a)