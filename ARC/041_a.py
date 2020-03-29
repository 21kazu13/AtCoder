def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
x,y = iim()
k = ii()

if k > y:
    print(x+y-(k-y))
else:
    print(x+k)