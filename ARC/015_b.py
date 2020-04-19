def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
l = [0]*6

for i in range(n):
    maxt, mint = map(float,input().split())
    if maxt >= 35.0:
        l[0] += 1
    elif maxt >= 30.0:
        l[1] += 1
    elif maxt >= 25.0:
        l[2] += 1
    elif maxt < 0:
        l[5] += 1
    
    if mint >= 25.0:
        l[3] += 1
    elif mint < 0 and maxt >= 0:
        l[4] += 1
print(' '.join(map(str, l)))

