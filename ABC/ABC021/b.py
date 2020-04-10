def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
a,b = iim()
k = ii()
P = iil()

if a in P or b in P:
    print('NO')
else:
    if len(set(P)) == len(P):
        print('YES')
    else:
        print('NO')
