def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a, b, k = iim()
l = []
if b-a+1 > 2*k:
    for i in range(a,a+k):
        l.append(i)
    for j in range(b-k+1,b+1):
        l.append(j)
else:
    for n in range(a,b+1):
        l.append(n)

for k in l:
    print(k)