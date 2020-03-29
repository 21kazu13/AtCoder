def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n,k = iim()
A = []
for i in range(n):
    A.append(ii())

sumwalk = 0
day = 0
for item in A:
    day += 1
    sumwalk += item
    if sumwalk >= k:
        print(day)
        exit()