def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
m = ii()
if m < 100:
#    print('a')
    print('00')
elif m <= 5000:
#    print('b')
    if m//100 < 10:
        print('0'+str(m//100))
    else:
        print(m//100)
elif m <= 30000:
#    print('c')
    print(m//1000+50)
elif m <= 70000:
#    print('d')
    print((m//1000-30)//5+80)
else:
#    print('e')
    print(89)