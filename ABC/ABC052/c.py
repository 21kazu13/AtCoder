def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

n = int(input())
mod = 1_000_000_007
d = {}
for i in range(2,n+1):
    l = factorization(i)
    for item in l:
        d[item[0]] = d.get(item[0],0)+item[1]
ans = 1
for j in d.values():
    ans *= j+1
    ans %= mod
print(ans)