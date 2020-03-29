s = []
s.append(100)
s.append(100)
s.append(200)
#print(s[0],s[1],s[2])
for i in range(3,20):
    s.append(s[i-1]+s[i-2]+s[i-3])
print(s[19])