def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

from math import gcd

mod = int(1e9+7)
n = ii()
cnd = {}
azero = 0
bzero = 0
allzero = 0
for _ in range(n):
    a,b = iim()
    if a == 0:
        if b != 0:
            azero += 1
        else:
            allzero += 1
    elif b == 0:
        bzero += 1            
    else:
        g = gcd(a,b)
        a //= g
        b //= g
        if a < 0:
            a *= -1
            b *= -1
        cnd[(a,b)] = cnd.get((a,b),0)+1


noreg = 0
if azero == 0 or bzero == 0:
    noreg += max(azero,bzero)
    ans = 1
else:
    ans = (2**azero%mod + 2**bzero%mod - 1)%mod
for k,item in cnd.items():
    a,b = k
    if b>0:
        m = cnd.get((b,-a),False)
        if m:
            ans *= (2**item%mod+2**m%mod-1)%mod
        else:
            noreg += item
    else:
        m = cnd.get((-b,a),False)
        if not m:
            noreg += item
print(int((ans*((2**noreg)%mod)-1+allzero)%mod))