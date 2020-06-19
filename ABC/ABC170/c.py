def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

x,n = iim()
p = set(iil())
for i in range(100):
    if x-i not in p:
        print(x-i)
        exit()
    elif x+i not in p:
        print(x+i)
        exit()
