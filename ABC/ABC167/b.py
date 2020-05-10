def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b,c,k = iim()
if k < a:
    print(k)
elif k <= a+b:
    print(a)
else:
    print(a+(k-a-b)*(-1))