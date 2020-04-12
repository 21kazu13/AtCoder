import math
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,k = iim()
if k != 0:
    num = math.log((2e12*k+1)/(k*a+1),k+1)
    print(math.ceil(num))
else:
    print(int(2e12-a))