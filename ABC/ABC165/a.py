def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

k = ii()
a,b = iim()
flag = False
for i in range(a,b+1):
    if i%k == 0:
        flag = True
        break
print('OK' if flag else 'NG')