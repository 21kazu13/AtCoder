def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()

tail = [item for i,item in enumerate(A) if i%2 == 0]
head = [item for i,item in enumerate(A) if i%2 == 1]
ans = head[::-1]+tail if n%2 == 0 else tail[::-1]+head
print(*ans)