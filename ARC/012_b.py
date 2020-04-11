def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,tv,kv,l = iim()
dist = l
for i in range(n):
    dist = kv * dist / tv
    if dist < 1e-6:
        print(0)
        exit()
print(dist)