def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n,m = iim()
mod = 1000_000_007

def prepare(n, MOD):
     # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
     
    return factorials, invs


fac,inv = prepare(max(n,m),mod)
if abs(n-m) == 1:
    print(fac[n]*fac[m]%mod)
elif abs(n-m) == 0:
    print(fac[n]*fac[m]*2%mod)
else:
    print(0)