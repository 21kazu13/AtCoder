def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
from math import pi,sin,cos
a,b,h,m = iim()
h += m/60

th_h = 2*pi*h/12
th_m = 2*pi*h

ah = a*complex(cos(th_h),sin(th_h))
bm = b*complex(cos(th_m),sin(th_m))
#print(ah,bm)
print(abs(ah-bm))