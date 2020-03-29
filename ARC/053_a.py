def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

h,w = iim()
print(h*(w-1)+w*(h-1))
