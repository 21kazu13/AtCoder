def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()
A = iil()
cnt = 0
for i,item in enumerate(A):
    if (i+1)%2==1 and item%2==1:
        cnt+=1
print(cnt)