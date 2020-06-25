def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

#1000000000000001
alpha = 'abcdefghijklmnopqrstuvwxyz'
n = ii()
tmp = n
ans = ''
while tmp > 26:
    ans += alpha[tmp%26-1]
    if tmp%26 == 0:
        tmp //= 26
        tmp -= 1
    else:
        tmp //= 26
#    print(ans,tmp)

ans += alpha[tmp%26-1]
print(ans[::-1])