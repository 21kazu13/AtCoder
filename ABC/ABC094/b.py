def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m,x = iim()
before = 0
after = 0
A = iil()
for i in A:
    if i < x:
        before += 1
    else:
        after += 1

print(min(before,after))