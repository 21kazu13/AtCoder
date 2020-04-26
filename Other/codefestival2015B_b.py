def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
l = [0 for i in range(m+1)]
A = iil()

for item in A:
    l[item] += 1


ans = l.index(max(l))
print('?' if max(l) < (n//2 + 1) else ans)