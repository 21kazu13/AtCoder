def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b,c,d,e = iim()
l = list(set([a+b+c,a+b+d,a+b+e,a+c+d,a+c+e,a+d+e,b+c+d,b+c+e,b+d+e,c+d+e]))
print(sorted(l,reverse=True)[2])
