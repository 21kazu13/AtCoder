def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m,x = iim()
l = []
A = list(range(n))

for _ in A:
    l.append(iil())

ans = 1e9
for i in range(1 << n):
    output = []
    for j in range(n):
        if ((i >> j) & 1) == 1:
            output.append(A[j])
    sc = [0]*(m+1)
    for k in output:
        sc = [x+y for x,y in zip(sc,l[k])]
    if min(sc[1:]) >= x:
        ans = min(ans,sc[0])
print(ans if ans < 1e9 else -1)