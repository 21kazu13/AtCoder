def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

a,b = iim()
l = [a-b,a+b,a*b]
l.sort()
print(l[-1])