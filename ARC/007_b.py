def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n,m = iim()
l = [i for i in range(n+1)]
for j in range(m):
    cd = ii()
    l[l.index(cd)] = l[0]
    l[0] = cd
for k in l[1::]:
    print(k)
