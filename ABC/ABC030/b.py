def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n,m = iim()
n = n%12

longer = 6*m
shorter = 30*n+0.5*m
deg = abs(longer-shorter)
print(deg if deg < 180 else 360-deg)
