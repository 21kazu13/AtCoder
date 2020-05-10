def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()

if n == 1 or m == 1:
    if n*m == 1:
        print(1)
    else:
        print(n*m-2)
else:
    print((n-2)*(m-2))