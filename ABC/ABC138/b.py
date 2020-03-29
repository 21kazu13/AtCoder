def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()

prod = 1
for item in A:
    prod *= item

frac = 0
for item in A:
    frac += prod//item

print(prod/frac)