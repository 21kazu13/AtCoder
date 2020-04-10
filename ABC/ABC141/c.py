def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,k,q = iim()
l = [k]*n
for i in range(q):
    p = ii()
    l[p-1] += 1

for j in l:
    if j < q+1:
        print('No')
    else:
        print('Yes')