def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
pmax = 0
psum = 0
for i in range(n):
    s,p = ism()
    p = int(p)
    psum += p
    if pmax < p:
        cand = s
        pmax = p
if 2*pmax > psum:
    print(cand)
else:
    print('atcoder')