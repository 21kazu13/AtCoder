def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
w,h = iim()
if w/h == 4.0/3.0:
    print('4:3')
else:
    print('16:9')