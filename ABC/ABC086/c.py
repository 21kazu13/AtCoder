def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
flag = True
for i in range(n):
    t,x,y = iim()
    if x+y > t or t%2 != (x+y)%2:
        flag = False

print('Yes' if flag else 'No')