n, k = map(int,input().split())
d = list(map(int,input().split()))
foruse = [0,1,2,3,4,5,6,7,8,9]
for item in d:
    foruse.remove(item)
#print(foruse)

for i in range(n,100000):
    flag = 1
#    print('test:'+str(i))
    for item in list(str(i)):
        if int(item) not in foruse:
            flag = 0
    if flag == 1:
        print(i)
        break

