n,m = map(int,input().split())
n -= m
print((1900*m+n*100)*2**m)