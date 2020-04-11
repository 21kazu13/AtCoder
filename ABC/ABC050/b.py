def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
T = iil()
m = ii()
drink = []
for i in range(m):
    drink.append(iil())

time = sum(T)
for item in drink:
    dif = item[1] - T[item[0]-1]
    print(time + dif)