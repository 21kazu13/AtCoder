def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n,x = iim()
if x<=n//2:
    print(x-1)
else:
    print(n-x)