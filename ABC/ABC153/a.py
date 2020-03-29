def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
h,a = iim()
if h%a == 0:
    f = 0
else:
    f = 1

print(h//a+f)