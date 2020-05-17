def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

h,w = iim()
n = ii()
A = iil()
ans = []
l = []
for i,item in enumerate(A):
    l += [i+1]*A[i]

for i in range(h):
    p = l[i*w:(i+1)*w]
    if i%2 == 1:
        ans.append(p[::-1])
    else:
        ans.append(p)

for i in ans:
    print(*i)
