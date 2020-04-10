def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

x1,y1,x2,y2 = iim()
difx = x2-x1
dify = y2-y1
x3 = x2-dify
y3 = y2+difx
x4 = x3-difx
y4 = y3-dify

print(x3,y3,x4,y4)
