def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

#from math import gcd
from fractions import Fraction as Fc
#FractionがTLE主要因ぽい。


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
        f = Fc(a,b)
        cnd[f] = cnd.get(f,0)+1


noreg = 0
if azero == 0 or bzero == 0:
    noreg += max(azero,bzero)
    ans = 1
else:
    ans = (2**azero%mod + 2**bzero%mod - 1)%mod

#print(cnd)
for k,item in cnd.items():
#    print(k)
    if k>0:
        m = cnd.get(Fc(-1,k),False)
        if m:
            ans *= (2**item%mod+2**m%mod-1)%mod
        else:
            noreg += item
    else:
        m = cnd.get(Fc(-1,k),False)
#        print(m,k,Fc(-1,k))
        if not m:
            noreg += item
#    print(ans,noreg)
print(int((ans*((2**noreg)%mod)-1+allzero)%mod))