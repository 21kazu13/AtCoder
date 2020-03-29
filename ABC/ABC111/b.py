n = input()
if len(set(list(n)))==1:
    print(n)
else:
    num = int(n[0])+int(n[0])*10+int(n[0])*100
    if int(n) < num:
        print(num)
    else:
        print(num+111)