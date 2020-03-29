def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

l1 = [1,3,5,7,8,10,12]
l2 = [4,6,9,11]
x,y = iim()

if (x in l1 and y in l1) or (x in l2 and y in l2):
    print('Yes')
else:
    print('No')