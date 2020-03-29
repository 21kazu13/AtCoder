s = input()
sum = int(s)
length = len(s)
inputlist = list(s)
#print(s)

for i in range(1,2**(length-1)):
    addlist = []
    addflag = format(i,'0'+str(len(s)-1)+'b')
    begin = 0
    for j in range(length-1):#max 9 items : index:0-8
        if addflag[j] == '1':
            addlist.append(s[begin:j+1])
            begin = j+1
        if j == length-2:#last index
            addlist.append(s[begin::])
    for item in addlist:
        sum += int(item)
print(sum)
