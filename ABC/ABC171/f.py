def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
k = ii()
s = input()
n = len(s)

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

fac,inv = prepare(n+k,mod)
ans = 26**n%mod
for i in range(1,min(n,k)+1):
    tmp = (26**(n-i))%mod
    tmp *= (25**i)%mod
    tmp *= (fac[k+1]*inv[k-i]*inv[i+1])%mod
    tmp *= (fac[n+1]*inv[n-i]*inv[i+1])%mod
    ans = (ans+tmp)%mod

print(ans)
