def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,a,b = iim()
ans = 0
for i in range(n):
    s,d = ism()
    d = int(d)
    if s == 'East':
        if d < a:
            ans += a
        elif d < b:
            ans += d
        else:
            ans += b
    else:
        if d < a:
            ans -= a
        elif d < b:
            ans -= d
        else:
            ans -= b
if ans > 0:
    print('East {}'.format(ans))
elif ans < 0:
    print('West {}'.format(abs(ans)))
else:
    print(0)