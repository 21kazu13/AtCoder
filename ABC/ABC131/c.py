def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

from fractions import gcd
a,b,c,d = iim()


def num(i):
    n = c*d//gcd(c,d)
    return i-i//c-i//d+i//n

print(num(b)-num(a-1))