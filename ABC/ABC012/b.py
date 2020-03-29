def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()
hour = n//3600
minu = (n-hour*3600)//60
seco = n-hour*3600-minu*60
print('{:02}:{:02}:{:02}'.format(hour,minu,seco))