def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
H = iil()
mh = 0
for i in H:
    if mh - 1 > i:
        print('No')
        exit()
    else:
        mh = max(mh,i)
print('Yes')