def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
l = []
for i in range(n):
    l.append(iil())

l.sort()
#print(l)
cost = 0
num = 0
for item in l:
    num += item[1]
    cost += item[0]*item[1]
#    print(num,cost)
    if num >= m:
        cost -= (num-m)*item[0]
        print(cost)
        exit()

