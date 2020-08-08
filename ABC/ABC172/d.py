def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
import copy
n = ii()
l = [None,None]

def factorization(n):
    d = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0 and temp//i != 1:
            d = copy.copy(l[temp//i])
            d[i] = d.get(i,0)+1
            break
    if len(d) == 0:
        d[n] = 1
    l.append(d)
    cnt = 1
    for item in d.values():
        cnt *= (item+1)
    return cnt

ans = 1
for i in range(2,n+1):
    print(i)
    tmp = factorization(i)
    ans += i*tmp
#    print(l)
print(ans)