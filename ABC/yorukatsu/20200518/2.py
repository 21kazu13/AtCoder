def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n,m = iim()
l =[]
for _ in range(n):
    l.append(iil())

l.sort()

num = 0
val = 0
for item in l:
    cst = item[0]
    cnt = item[1]
    if num + cnt < m:
        val += cst*cnt
        num += cnt
    else:
        val += cst*(m-num)
        break
print(val)
#100000000000000
#100000000000000
