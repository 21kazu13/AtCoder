def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

E = iil()
B = ii()
L = iil()

cnt = 0
for i in L:
    if i in E:
        cnt += 1

if cnt == 6:
    print(1)
elif cnt == 5:
    print(2 if B in L else 3)
elif cnt > 2:
    print(8-cnt)
else:
    print(0)