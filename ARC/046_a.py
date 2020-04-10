l = list(range(1,10))
for i in range(10,55):
    if i%10 == 9:
        continue
    num = int(str(l[i%10])*(i//10+1))
    l.append(num)
#    print(i,num)
n = int(input())
print(l[n-1])