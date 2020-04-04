def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()

def S(n):
    if n==0: return 0
    else:
        l = len(str(n))
        s = n//(10**(l-1))
        return s+S(n%(10**(l-1)))
if n%S(n) == 0:
    print('Yes')
else:
    print('No')