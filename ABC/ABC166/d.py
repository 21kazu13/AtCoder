def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

x = ii()
l = [0]
i = 0
num = 0
while num < 10**11:
    i += 1
    num = i**5
    l.append(num)
#print(l[-1]-l[-2])
#これが10**9より大きい必要がある
l = set(l)
for item in l:
    if item > x:
        if item - x in l:
            print(int(item**0.2),int((item-x)**0.2))
            exit()
    else:
        if x - item in l:
            print(int(item**0.2),int((x-item)**0.2)*(-1))
            exit()

'''
    if x - item in l:#Aがitemでx-itemは-B**5
        print(int(item**0.2),int(abs(item-x)**0.2)*(-1))
        exit()
    elif item - x in l:#Aがitemでx-itemはB**5
#        print(item,item-x)
        print(int(item**0.2),int(abs(item-x)**0.2)*(-1))
        exit()
'''