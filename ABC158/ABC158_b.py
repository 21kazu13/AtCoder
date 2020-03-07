n,a,b = map(int, input().split())
trial = a+b
num = int(n/trial)
rest = min(a,n%trial)
#print(rest)
print(a*num+rest)