def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

from fractions import Fraction

mod = 1e9+7
n = ii()
cnd = {}
azero = 0
bzero = 0
for _ in range(n):
    a,b = iim()
    if a*b == 0:
        if a == 0 and b != 0:
            azero += 1
        elif a != 0 and b == 0:
            bzero += 1
    else:
        ratio = Fraction(a,b)
        before = cnd.get(ratio,False)
        check = cnd.get(-1*Fraction(1,ratio),False)
        if before:
            cnd[ratio] = [before[0]+1,before[1]]
        elif check:
            cnd[-1*Fraction(1,ratio)] = [check[0],check[1]+1]
        else:
            cnd[ratio] = [1,0]

cnd[0] = [azero,bzero]
noreg = 0
ans = 1
#print(cnd)
for item in cnd.values():
    if item[0] == 0  or item[1] == 0:
        noreg += max(item[0],item[1])
    else:
        ans *= (2**item[0]+2**item[1]-1)
        ans %= mod
#print(ans,noreg)
print(int((ans*((2**noreg)%mod)-1)%mod))