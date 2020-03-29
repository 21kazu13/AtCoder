def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

a=ii()
b=ii()
c=ii()
l = sorted([a,b,c],reverse=True)

print(l.index(a)+1)
print(l.index(b)+1)
print(l.index(c)+1)
