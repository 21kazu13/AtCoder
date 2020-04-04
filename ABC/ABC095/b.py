def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,x = iim()
total = 0
lowest = 100001
for i in range(n):
    m = ii()
    total += m
    lowest = min(lowest,m)
print(n+(x-total)//lowest)