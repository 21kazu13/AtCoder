def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
a = ii()
b = ii()
if a%b != 0:
    print(b-a%b)
else:
    print(0)