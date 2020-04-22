def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b,c = iim()

l = [i*(a%b)%b for i in range(b)]
#print(l)
print('YES' if c in l else 'NO')
