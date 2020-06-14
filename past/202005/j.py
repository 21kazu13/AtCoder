def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

def binarySearch(l,item):
    '''
    O(log(len(l)))
    l : list sorted by "desc"
    item : target of search
    '''
    left = 0
    right = len(l)-1
    if item > l[0]:
        return 0
    if item <= l[-1]:
        return -2
    while right != left+1:
        mid = (left+right)//2
        cnd = l[mid]
        if cnd >= item:
            left = mid
        if cnd < item:
            right = mid
    return right

n,m = iim()
l = [-1]*n
A = iil()
ans = []
for i,item in enumerate(A):
    ans.append(binarySearch(l,item))
    if ans[-1] >= 0:
        l[ans[-1]] = item
#    print(l)
#    print(ans)

for j in ans:
    print(j+1)