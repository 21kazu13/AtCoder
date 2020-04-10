def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
l = []
mod = []
for i in range(5):
    num = ii()
    l.append((num+9)//10*10)
    if num%10 == 0:
        mod.append(10)
    else:
        mod.append(num%10)
a = 10-min(mod)
print(sum(l)-a)

