def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

def binary_search(lis, item):
    low = 0
    high = len(lis) - 1
    inRange = high

    if lis[0] > item:
        return 0

    while low <= high:
        mid = (low + high) //2
        guess1 = lis[mid]
        if mid < inRange:
            guess2 = lis[mid+1]
        else:
            if lis[mid] <= item:
                return len(lis)
            else:
                return len(lis)-1
        if guess1 <= item < guess2:
            return mid+1
        if guess1 > item:
            high = mid-1
        else:
            low = mid+1
    return 0

n,m,k = iim()
a = iil()
cuma = []
if a[0] <= k:
    cuma.append(a[0])
    for i in range(n-1):
        num = cuma[-1]+a[i+1]
        if num > k:
            break
        else:
            cuma.append(num)
b = iil()
cumb = []
if b[0] <= k:
    cumb.append(b[0])
    for i in range(m-1):
        num = cumb[-1]+b[i+1]
        if num > k:
            break
        else:
            cumb.append(num)

ans = len(cumb)
if len(cuma) > 0:
    cnt = len(cuma)
    for i,item in enumerate(cuma[::-1]):
        tmp = cnt-i
        res = k-item
        plus = binary_search(cumb,res)
        ans = max(ans,tmp+plus)
print(ans)
