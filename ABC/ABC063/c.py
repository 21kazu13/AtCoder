def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
l = []
for i in range(n):
    l.append(ii())

l.sort()
sA = sum(l)
if sA%10 != 0:
    print(sA)
else:
    lis = [i for i in l if i%10 != 0]
    if len(lis) == 0:
        print(0)
    else:
        print(sA - min(lis))