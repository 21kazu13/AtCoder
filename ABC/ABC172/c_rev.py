def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

import numpy as np

def binarySearch(lis,key):
    '''
    二分探索
    O(log(m)):m=len(lis)
    降順もしくは昇順ソートになってる必要あり
    '''
    ng = -1
    ok = len(lis)
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if isOk(mid,key): ok = mid
        else: ng = mid
    '''
    okはisOkで定義した条件を満たす最小の値
    ngはisOkで定義した条件を満たさない最大の値
    '''
    return ok

def isOk(lis,index,key):
    '''
    binarySearch 用
    if節の条件は、必要に応じて変更の必要あり
    '''
    if lis[index] > key: return True
    else: return False

n,m,k = iim()
a = iil()
cuma = np.cumsum(a)
b = iil()
cumb = np.cumsum(b)

ans = binarySearch(cumb,k)
for i,item in enumerate(cuma):
    if item > k:
        break

    res = k-item
    plus = binarySearch(cumb,res)
    ans = max(ans,i+1+plus)

print(ans)
