def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = [0]+iil()+[0]

cst = 0
for i in range(1,n+2):
    cst += abs(A[i]-A[i-1])

for i in range(1,n+1):
    minus = abs(A[i]-A[i-1])+abs(A[i+1]-A[i])
    plus = abs(A[i+1]-A[i-1])
    print(cst+plus-minus)