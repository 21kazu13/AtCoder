k = int(input())

def forndigit(l1):
    l = []
    for i in l1:
        if i[-1] == '1':
            l.append(i+'0')
            l.append(i+'1')
            l.append(i+'2')
        elif i[-1] == '2':
            l.append(i+'1')
            l.append(i+'2')
            l.append(i+'3')
        elif i[-1] == '3':
            l.append(i+'2')
            l.append(i+'3')
            l.append(i+'4')
        elif i[-1] == '4':
            l.append(i+'3')
            l.append(i+'4')
            l.append(i+'5')
        elif i[-1] == '5':
            l.append(i+'4')
            l.append(i+'5')
            l.append(i+'6')
        elif i[-1] == '6':
            l.append(i+'5')
            l.append(i+'6')
            l.append(i+'7')
        elif i[-1] == '7':
            l.append(i+'6')
            l.append(i+'7')
            l.append(i+'8')
        elif i[-1] == '8':
            l.append(i+'7')
            l.append(i+'8')
            l.append(i+'9')
        elif i[-1] == '9':
            l.append(i+'8')
            l.append(i+'9')
        elif i[-1] == '0':
            l.append(i+'0')
            l.append(i+'1')
    return l

l1 = [str(i) for i in range(1,10)]
r = [l1]
for i in range(2,11):
    r.append(forndigit(r[i-2]))
ans = []
for item in r:
    ans += item
print(ans[k-1])