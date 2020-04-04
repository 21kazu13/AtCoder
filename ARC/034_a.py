def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
highest = 0
for i in range(n):
    a,b,c,d,e = iim()
    highest= max(a+b+c+d+(e*110/900),highest)

print(highest)