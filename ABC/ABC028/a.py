def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()

if n < 60:
    print('Bad')
elif n < 90:
    print('Good')
elif n < 100:
    print('Great')
else:
    print('Perfect')