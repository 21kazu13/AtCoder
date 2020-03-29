def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
a,b,c = iim()
for i in range(1,128):
    if i%3 == a and i%5 == b and i%7 == c:
        print(i)