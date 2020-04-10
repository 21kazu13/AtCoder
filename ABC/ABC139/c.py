def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
H = iil()

cnt = 0
ans = 0

for i in range(1,len(H)):
#    print(i)
    if H[i-1] >= H[i]:
#        print('hoge')
        cnt += 1
    else:
        ans = max(cnt,ans)
        cnt = 0
print(max(cnt,ans))