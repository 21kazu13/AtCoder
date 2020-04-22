def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()
ans = 0

l = [0]*(max(A)+2)

for i in A:
    if i != 0:
        l[i-1] += 1
    l[i] += 1
    l[i+1] += 1
#print(l)
print(max(l))