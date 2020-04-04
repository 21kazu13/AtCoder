def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,l = iim()
aji = 0
flag = False

for i in range(1,n+1):
    if l+i-1 == 0:
        flag = True
    aji += l+i-1


if flag:
    print(aji)
elif l > 0:
    print(aji - l)
else:
    print(aji - (l+n-1))