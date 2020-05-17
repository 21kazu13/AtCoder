def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
import fractions
a,b,c,d = iim()

def antiDiv(n):
    return n-n//c-n//d+n//(c*d//fractions.gcd(c,d))
print(antiDiv(b)-antiDiv(a-1))