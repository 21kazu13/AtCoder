x = int(input())
num = 0
for i in range(1,1000000):
    num += i
    if num >= x:
        print(i)
        exit() 