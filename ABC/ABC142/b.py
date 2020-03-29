def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n,k = iim()
h = iil()

ok = [i for i in h if i >= k]
print(len(ok))