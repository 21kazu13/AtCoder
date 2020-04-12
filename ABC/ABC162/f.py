def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
A = iil()

if n%2 == 0:
    print(max(sum(A[::2]),sum(A[1::2])))
else:
    for i,item in enumerate(A):
        #奇数の時は難しそう
        print('hoge')