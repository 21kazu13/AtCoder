#import math
import fractions
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,x = iim()
xmod = list(map(lambda y:abs(int(y)-x),input().split()))
#print(xmod)
gcd = xmod[0]
for i in xmod:
    gcd = fractions.gcd(gcd,i)

print(gcd)