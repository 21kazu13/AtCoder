def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
cnt = 0
n,d = iim()

for _ in range(n):
    x,y = iim()
    if x**2+y**2 <= d**2:
        cnt += 1

print(cnt)