def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
W = iil()
sW = sum(W)
div = 0
for i in W:
    div += i
    if div > (sW+1)//2:
        print(min(2*div-sW, sW-2*(div-i)))
        exit()