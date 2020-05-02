def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
if m == 1:
    print(1,2)
elif n%2 == 1:
    l = list(range(1,n//2+1))[::-1]
#    print(l)
    for i in l[:m]:
        print(i,n-i)
else:
    for i in range(1,m):
        print(i,n-i+1)
    print(m,n//2)
