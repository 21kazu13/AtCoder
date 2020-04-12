def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
s = {'i','n','d','e','o','w'}
l = ['d','d','e','e','i','n','n','o','w']
ans = []
for i in range(n):
    st = input()
    if set(st) != s:
        ans.append(False)
    else:
        if sorted(list(st)) == l:
            ans.append(True)
        else:
            ans.append(False)

for j in ans:
    print('YES' if j else 'NO')