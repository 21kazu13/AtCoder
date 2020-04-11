def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
l = []
for i in range(n):
    tmp = isl()
    tmp.append(i+1)
    l.append(tmp)
#print(l)
l = sorted(l,key=lambda x:int(x[1]),reverse=True)
#print(l)
l = sorted(l,key=lambda x:x[0])
#この2回ソートは、降順と昇順が混ざるのであれば必須っぽい
#https://www.haya-programming.com/entry/2018/07/20/095759
for j in l:
    print(j[2])