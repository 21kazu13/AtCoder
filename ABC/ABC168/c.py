def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
import math
a,b,h,m = iim()

th_m = 6*m
th_h = 30*h+0.5*m

theta = abs(th_m-th_h) if abs(th_m-th_h)<180 else 360-abs(th_m-th_h)
#print(th_m-th_h)

l = a**2+b**2-2*a*b*math.cos(math.radians(theta))
print(l**0.5)