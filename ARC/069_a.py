def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
if 2*n > m:
    print(m//2)
else:
    print(n+(m-2*n)//4)