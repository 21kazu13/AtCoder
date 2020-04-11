def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

y = ii()
m = ii()
if m < 3:
    m += 12
    y -= 1
d = ii()

def psDays(y,m,d):
    ret = -429
    ret += 365*y
    ret += (y//4 - y//100 + y//400)
    ret += d
    ret += (306*(m+1) // 10)
    return ret

print(psDays(2014,5,17)-psDays(y,m,d))