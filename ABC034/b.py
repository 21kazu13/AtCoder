def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n = ii()
if n%2 == 0:
    print(n-1)
else:
    print(n+1)