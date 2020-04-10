def colsum(n):
    ret = 0
    num = n
    while num >= 10:
        ret += num%10
        num //= 10
    ret += num
    return ret

def iim():return map(int,input().split())

n,a,b = iim()
cnt = 0
for i in range(1,n+1):
    if a <= colsum(i) <= b:
        cnt += i
print(cnt)