def ii():return int(input())
def isl():return list(map(str,input().split()))
n = ii()
words = isl()
words[-1] = words[-1][:len(words[-1])-1]
l = ['takahashikun','TAKAHASHIKUN','Takahashikun']
ans = 0
for item in words:
#    print(item)
    if item in l:
        ans += 1
print(ans)