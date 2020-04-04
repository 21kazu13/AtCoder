def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n,x = iim()
A = sorted(iil())
count = 0
for i in A:
    x -= i
    count += 1
    if x < 0:
        print(count-1)
        exit()
    elif x == 0:
        print(count)
        exit()
print(count-1)