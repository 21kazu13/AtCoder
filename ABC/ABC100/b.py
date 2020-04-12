def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

d,n = iim()
num = 0
for i in range(n):
    num += 100**d
    if num%100**(d+1) == 0:
        num += 100**d
print(num)