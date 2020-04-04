def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
d,x = iim()
count = 0
for i in range(n):
    a = ii()
    if d%a == 0:
        count += d//a
    else:
        count += d//a + 1
print(count+x)