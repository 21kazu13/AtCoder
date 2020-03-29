def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b =iim()
tb = 0
for i in range(1,b-a+1):
    tb += i
#普通(b-a)*(b-a+1)//2で求めろよね、
print(tb-b)