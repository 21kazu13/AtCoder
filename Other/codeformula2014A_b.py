l = ['x']*10
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b = iim()
p = iil()
q = iil()

for i in p:
    l[i-1] = '.'
for j in q:
    l[j-1] = 'o'

print(' '.join(l[6::]))
print(' '+' '.join(l[3:6:]))
print(' '+' '+' '.join(l[1:3:]))
print(' '+' '+' '+str(l[0]))