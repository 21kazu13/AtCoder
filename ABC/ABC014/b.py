def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,x = iim()
s = list(format(x,'0'+str(n)+'b'))
A = iil()
ans = 0
for i,item in enumerate(s[::-1]):
    if item == '1':
        ans += A[i]

print(ans)