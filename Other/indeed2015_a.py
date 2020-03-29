import math

def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

x1,y1 = iim()
x2,y2 = iim()

print(abs(x1-x2)+abs(y1-y2)+1)