def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
h,n = iim()
A = iil()
if h > sum(A):
    print('No')
else:
    print('Yes')