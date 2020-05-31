def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

def cntUru(num):
    mul4 = num//4
    mul100 = num//100
    mul400 = num//400

    return mul4-mul100+mul400

a,b = iim()
print(cntUru(b)-cntUru(a-1))