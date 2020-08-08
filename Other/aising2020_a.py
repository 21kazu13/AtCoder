def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

l,r,d = iim()
lf = l//d
lmod = l%d
rf = r//d

if lf == rf:
    print(1 if lmod == 0 else 0)
else:
    print(rf-lf if lmod !=0 else rf-lf+1)