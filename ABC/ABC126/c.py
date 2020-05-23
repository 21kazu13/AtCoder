def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,k = iim()
ans = 0
for i in range(1,min(k,n+1)):
    num = i
    cnt = 0
    while num<k:
        cnt += 1
        num *= 2
#    print(0.5**cnt)
    ans += 0.5**cnt

ans += max(n-k+1,0)
print(ans/n)
