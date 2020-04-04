s = input()
y,m,d = map(int,s.split('/'))

days = [31,28,31,30,31,30,31,31,30,31,30,31]
if y%400 == 0 or (y%100 != 0 and y%4 ==0):
    days[1] = 29   

if y%(m*d) == 0:
    print(s)
else:
    for day in range(d,days[m-1]+1):
        if y%(m*day) == 0:
            print('{}/{:02}/{:02}'.format(y,m,day))
            exit()
    for month in range(m+1,13):
        for day in range(1,days[m-1]+1):
            if y%(month*day) == 0:
                print('{}/{:02}/{:02}'.format(y,month,day))
                exit()
    print('{}/01/01'.format(y+1))