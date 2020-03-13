import math
import sys

n = int(input())
s = int(input())

up = math.sqrt(n)

def colsum(num, base):
    if num < base:
        return num
    else:
        return num%base + colsum(num//base,base)

#s >= n
if s == n:
    print(n+1)
elif s > n:
    print(-1)
else:
    #sqrt(n)まで探索
    for i in range(2,int(up)+1):
        if colsum(n,i) == s:
            print(i)
            sys.exit()

    #2桁しかあり得ない場合(sqrt(n)<b<n)
    for j in range(int(up),0,-1):
        # bが小さいやつを出したいんだからjは大きい方から。
        # j=1までなんだからrangeは0まで指定してj=1が含められるようにする。
        if (n-s)%j == 0:
            b = (n-s)/j + 1
            if colsum(n,b) == s and b > 1:
                print(int(b))
                sys.exit()

    print(-1)