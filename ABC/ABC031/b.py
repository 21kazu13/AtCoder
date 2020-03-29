def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

l,h = iim()
n = ii()
A = []
for i in range(n):
    A.append(ii())

for item in A:
    if item < l:
        print(l-item)
    elif item > h:
        print(-1)
    else:
        print(0)