def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

x,y = iim()
if y%2 == 0 and 2*x<=y<=4*x:
    print('Yes')
else:
    print('No')