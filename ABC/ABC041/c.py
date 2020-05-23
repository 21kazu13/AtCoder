def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()
l = []
for i,item in enumerate(A):
    l.append([item,i+1])

l.sort(reverse=True)

for j in l:
    print(j[1])
