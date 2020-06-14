def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

a,r,n = iim()

if r == 1:
    print(a)
else:
    if n > 40:
        print('large')
    else:
        ans = a*r**(n-1)
        print('large' if ans > 1e9 else ans)