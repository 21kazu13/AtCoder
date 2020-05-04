def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,k = iim()
l = [True]*n
for i in range(k):
    d = ii()
    A = iil()
    for item in A:
        if l[item-1] == True:
            l[item-1] = False

print(l.count(True))