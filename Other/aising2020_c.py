def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()
l = [0]*10001
for x in range(1,100):
    for y in range(x,100):
        for z in range(y,100):
            num = x**2+y**2+z**2+x*y+y*z+z*x
            if num < 10001:
                if x==y and y==z:
                    l[num] += 1
                elif x==y or y==z:
                    l[num] += 3
                else:
                    l[num] += 6

for i in l[1:n+1]:
    print(i)