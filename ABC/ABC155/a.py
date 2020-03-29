def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
aset = set(sorted(iil()))
if len(aset) == 2:
    print('Yes')
else:
    print('No')