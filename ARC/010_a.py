def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m,a,b = iim()
day = 0
card = n
for i in range(m):
    day += 1
    if card <= a:
        card += b
    card -= ii()
    if card < 0:
        print(day)
        exit()
print('complete')